import sys
import logging
from nose.plugins import Plugin

log = logging.getLogger(__name__)

def trace_fn(frame, event, args):
    print event, args
    return trace_fn

class Nostrils(Plugin):
    name = 'nostrils'

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)
        if self.enabled:
            pass

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)

    def addError(self, test, err, *a):
        self._restore_tracefn()

    def addFailure(self, test, err):
        self._restore_tracefn()

    def addSkip(self, test, err):
        self._restore_tracefn()

    def addSuccess(self, test, err):
        self._restore_tracefn()

    def startTest(self, test):
        self._install_tracefn(trace_fn)

    def _install_tracefn(self, tracefn):
        sys.settrace(tracefn)

    def _restore_tracefn(self):
        sys.settrace(None) # TODO be a good citizen
