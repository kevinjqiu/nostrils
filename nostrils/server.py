from wsgiref.simple_server import make_server

def nostril_server(environ, start_response):
    if environ['PATH_INFO'] == '/fail':
        body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return 'failure notified. %s' % body
    elif environ['PATH_INFO'] == '/error':
        body = environ['wsgi.input'].read(int(environ['CONTENT_LENGTH']))
        start_response('200 OK', [('Content-Type', 'text/plain')])
        return 'error notified'
    else:
        start_response('404 Not Found', [('Content-Type', 'text/plain')])
        return ''

if __name__ == '__main__':
    # for local testing
    make_server('localhost', 8000, nostril_server).serve_forever()
