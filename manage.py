from wsgi import Application
from settngs import ROUTES, FRONTS

def application(environ, start_response):
    app = Application(ROUTES, FRONTS)
    return app(environ, start_response)


