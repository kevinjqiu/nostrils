import logging
from wsgiref.simple_server import make_server
from functools import wraps
from nostrils.server.notify import send_notification

log = logging.getLogger(__name__)

ROUTE_MAP = {}

def handles(route):
    def decorator(f):
        ROUTE_MAP[route] = f
        @wraps(f)
        def wrapper(environ, response):
            return f(environ, response)

    return decorator

@handles(('POST', '/fail'))
def on_fail(environ, response):
    body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
    send_notification('Error', body)
    return response('200 OK', body=['Error notified'])

@handles(('GET', '/ping'))
def ping(environ, response):
    return response('200 OK', body=['pong'])

def nostril_server(environ, start_response):
    def response(status, content_type='text/plain', body=''):
        start_response(status, [('Content-Type', content_type)])
        return body

    path = environ['PATH_INFO']
    method = environ['REQUEST_METHOD']

    if (method, path) in ROUTE_MAP.keys():
        handler = ROUTE_MAP[(method, path)]
        return handler(environ, response)
    else:
        return response('404 Not Found')

def start_server(port):
    make_server('localhost', port, nostril_server).serve_forever()
    log.info('Nostril server started on port %d' % port)
