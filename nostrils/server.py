import logging
from wsgiref.simple_server import make_server
from pynotify import Notification

log = logging.getLogger(__name__)

def handle(type_, response, environ):
    body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
    n = Notification('Error', body)
    n.show()
    log.info(body)
    response('200 OK', [('Content-Type', 'text/plain')])
    return ['%s notified' % type_]

def nostril_server(environ, start_response):
    if environ['PATH_INFO'] == '/fail':
        handle('failure', start_response, environ)
    elif environ['PATH_INFO'] == '/error':
        handle('error', start_response, environ)
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ''

if __name__ == '__main__':
    # for local testing
    make_server('localhost', 8000, nostril_server).serve_forever()
