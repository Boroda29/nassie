import datetime

from nassie.common import templator
from nassie.consts import CONTENT_TYPE_TEXT_HTML, ENCODING, STATUS_CODE


class Application:

    class Error404:
        def __init__(self):
            self.name_template = "404.html"

        def __call__(self, request):
            request['TITLE'] = "404"
            request['PAGE'] = self.name_template
            body = templator.render(self.name_template, content=request)
            return STATUS_CODE["404"], body

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        print(f"--------START: {datetime.datetime.now()} ---------")
        print(f"-------- environ ---------\n{environ}\n-------- environ ---------")

        path = environ["PATH_INFO"]
        request = {}
        for front in self.fronts:
            front(request, env=environ)

        view = self.Error404()

        if path in self.routes:
            view = self.routes[path]
        code, body = view(request)
        print(request)
        start_response(code, [CONTENT_TYPE_TEXT_HTML])
        return [bytes(body, encoding=ENCODING)]


if __name__ == '__main__':
    print(__name__)
