import linecache
import sys
import logging
from nose.plugins import Plugin
from collector import TraceCollector

log = logging.getLogger(__name__)


class Tracer(object):

    def __init__(self, collector):
        self._collector = collector

    def __call__(self, frame, event, args):
        if event == 'line':
            self._trace_down(frame)
        return self.__call__

    def _trace_down(self, frame):
        # TODO: Probably not a good design to ask
        # collector for the current test context.
        test = self._collector.current_test

        while frame is not None:
            # If we have traced to the frame where
            # the test case was invoked,
            # stop there, because everything down-wards
            # isn't interesting to us.
            if frame.f_code == test.__call__.func_code:
                break
            self._collector.collect(frame)
            frame = frame.f_back

    def start(self):
        self._old_tracefn = sys.gettrace()
        sys.settrace(self.__call__)

    def stop(self):
        sys.settrace(self._old_tracefn)


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
                print "%s%s: %s" % (' ' * 2, lineno, line.rstrip())
                for testid in data[filename][lineno]:
                    print "%s* %s" % (' ' * 4, self._collector.get_test_case_name_by_id(testid))
                print "\n"

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)
        parser.add_option(
            '--nostrils-whitelist',
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
        self._collector.current_test = test
        self._tracer.start()

    def finalize(self, result):
        self._print()
        self._collector.save()
