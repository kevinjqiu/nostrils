import sys
import logging
from nose.plugins import Plugin
from collections import defaultdict

log = logging.getLogger(__name__)

class Nostrils(Plugin):
    name = 'nostrils'

    def __init__(self):
        super(Nostrils, self).__init__()
        # {file : { lineno : set([test_case_name])}}
        self._data = defaultdict(
            lambda : defaultdict(
                lambda : []
            )
        )

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)

        if self.enabled:
            pass

    def _trace_down(self, frame):
        while frame is not None:
            filename, lineno = frame.f_code.co_filename, frame.f_lineno
            if filename.endswith('worker.py'):
                self._data[filename][lineno].append(self._current_test)

            frame = frame.f_back

    def _trace(self, frame, event, args):
        if event == 'line':
            self._trace_down(frame)
        return self._trace

    def _print(self):
        for filename in self._data.keys():
            print "File: %s" % filename
            for lineno in sorted(self._data[filename].keys()):
                print "  %s:%s" % (lineno, self._data[filename][lineno])

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)

    def addError(self, test, err, *args):
        self._restore_tracefn()

    def addFailure(self, test, err, *args):
        self._restore_tracefn()

    def addSkip(self, test, err):
        self._restore_tracefn()

    def addSuccess(self, test, err):
        self._restore_tracefn()

    def startTest(self, test):
        self._current_test = test
        self._install_tracefn()

    def finalize(self, result):
        self._print()

    def _install_tracefn(self):
        self._orig_tracefn = sys.gettrace()
        sys.settrace(self._trace)

    def _restore_tracefn(self):
        sys.settrace(self._orig_tracefn)
