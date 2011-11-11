import logging
import json
from wsgiref.simple_server import make_server
from functools import wraps
from nostrils.server.notify import send_notification

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

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
    try:
        info = json.loads(body)
        title = ": ".join((info['type'], info['test_name']))
        send_notification(title, info['top_stackframe'])
        return response('200 OK', body=['Error notified'])
    except:
        log.info('Bad content received: "%s"' % body)
        return response('500 Internal Server Error', [''])

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
    log.info('Nostril server started on port %d' % port)
    try:
        make_server('localhost', port, nostril_server).serve_forever()
    except KeyboardInterrupt:
        log.info('Nostril server terminated by user request')