import logging
import httplib
import json
from nose.plugins import Plugin

log = logging.getLogger(__name__)

class Nostrils(Plugin):
    name = 'nostrils'

    def configure(self, options, conf):
        super(Nostrils, self).configure(options, conf)
        self.nostrils_server = options.nostrils_server

    def add_options(self, parser, env=None):
        super(Nostrils, self).add_options(parser, env)
        parser.add_option('-n', '--nostrils-server', dest='nostrils_server', help='nostrils server location')

    def addFailure(self, test, err, *args):
        conn = httplib.HTTPConnection(self.nostrils_server)
        conn.request("POST", "/fail", json.dumps({'test':str(test)}))
        response = conn.getresponse()
        log.info(response)
