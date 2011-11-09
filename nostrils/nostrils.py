from nose.plugins import Plugin
import logging

log = logging.getLogger(__name__)

class Nostrils(Plugin):
    name = 'nostrils'

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)

    def addFailure(self, test, err, *args):
        pass
