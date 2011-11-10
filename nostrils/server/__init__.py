from optparse import OptionParser
from nostrils.server.server import start_server

DEFAULT_PORT = 6000

def configure(args=None):
    parser = OptionParser()
    parser.add_option('-v', '--verbose', dest='verbose', action='store_true')
    parser.add_option('--port', dest='port', type='int', default=DEFAULT_PORT)
    options, args = parser.parse_args(args)
    return options

def main():
    options = configure()
    if options.verbose:
        import logging
        from nostrils.server.server import log
        log.setLevel(logging.INFO)
    start_server(options.port)

if __name__ == '__main__':
    main()
