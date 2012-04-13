import linecache

import os
import sys
import logging
from nose.plugins import Plugin
from collections import defaultdict

log = logging.getLogger(__name__)

CWD = os.getcwd()

class Tracer(object):

    def __init__(self, collector):
        self._collector = collector

    def __call__(self, frame, event, args):
        if event == 'line':
            self._trace_down(frame)
        return self.__call__

    def _trace_down(self, frame):
        while frame is not None:
            self._collector.collect(frame)
            frame = frame.f_back

    def start(self):
        self._old_tracefn = sys.gettrace()
        sys.settrace(self.__call__)

    def stop(self):
        sys.settrace(self._old_tracefn)

class TraceCollector(object):

    def __init__(self, whitelist=[]):
        # { filename : { lineno : [test_case_name] }}
        self._data = defaultdict(
            lambda : defaultdict(
                lambda : set([])
            )
        )
        self._whitelist = whitelist

    def should_collect(self, frame):
        if self._whitelist == '*':
            return True

        filename = frame.f_code.co_filename

        for folder in self._whitelist:
            if filename.startswith(os.path.join(CWD, folder)):
                return True

        return False

    def collect(self, frame):
        filename, lineno = frame.f_code.co_filename, frame.f_lineno
        if self.should_collect(frame):
            self._data[filename][lineno].add(self._current_test.address())

class Nostrils(Plugin):

    name = 'nostrils'

    def __init__(self):
        super(Nostrils, self).__init__()
        self._tracer = None
        self._collector = None

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)

        if self.enabled:
            whitelist = '*' if options.whitelist == '*' else options.whitelist.split(',')
            self._collector = TraceCollector(whitelist)
            self._tracer = Tracer(self._collector)

    def _print(self):
        data = self._collector._data
        for filename in data:
            print "File: %s" % filename
            for lineno in sorted(data[filename].keys()):
                line = linecache.getline(filename, lineno)
                tests = ["%s:%s.%s" % (file_, module, func) for file_, module, func in data[filename][lineno]]
                print "  %s" % line
                print "  %s:%s" % (lineno, tests)
                print "\n"

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)
        parser.add_option('--nostrils-whitelist',
            dest='whitelist',
            help='A comma separated list of top-level folders to be included, or "*" indicating "all".',
            default='*')

    def addError(self, test, err, *args):
        self._tracer.stop()

    def addFailure(self, test, err, *args):
        self._tracer.stop()

    def addSkip(self, test, *args):
        self._tracer.stop()

    def addSuccess(self, test, *args):
        self._tracer.stop()

    def startTest(self, test):
        self._collector._current_test = test
        self._tracer.start()

    def finalize(self, result):
        self._print()
