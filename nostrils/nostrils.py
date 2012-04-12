import logging
from nose.plugins import Plugin

log = logging.getLogger(__name__)

class Nostrils(Plugin):
    name = 'nostrils'

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)
        if self.enabled:
            try:
                import coverage
            except ImportError:
                log.error('Coverage not available:unable to import coverage module')
                self.enabled = False
                return
            self.conf = conf

            if self.enabled:
                self.coverage_instance = coverage.coverage(auto_data=False)

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)

    def begin(self):
        self.coverage_instance.load()
        self.coverage_instance.start()
