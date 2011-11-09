from nose.plugins import Plugin

class Nostrils(Plugin):
    name = 'nostrils'

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)

    def addFailure(self, test, err, *args):
        import pdb; pdb.set_trace()
