import datetime

from settngs import ROUTES, FRONTS
from nassie.controllers.pages import Error404
from nassie.constants import CONTENT_TYPE_TEXT_HTML, ENCODING, MAP_ENV_DATA_WSGI
from nassie.controllers.fronts import FrontControllerApp


class Application:
    def __init__(self, env):
        self.routes = ROUTES
        self.fronts = [FrontControllerApp.add_attr_pages,
                       FrontControllerApp.get_method_data_request]
        self.data_env = {}

        for method in FRONTS:
            self.fronts.append(method)

        for key, val in MAP_ENV_DATA_WSGI.items():
            self.data_env[val] = None
            obj_item = env.get(key)
            if obj_item:
                self.data_env[val] = obj_item

    def call_as(self, start_response):
        print(f"--------START: {datetime.datetime.now()} ---------")
        print(f"-------- environ ---------\n{self.data_env}\n-------- environ ---------")

        path_info = self.data_env["PATH_INFO"]
        request = {}
        for front in self.fronts:
            front(request, env=self.data_env)
        view = Error404()

        if path_info in self.routes:
            view = self.routes[path_info]
        code, body = view.view_as(request)
        start_response(code, [CONTENT_TYPE_TEXT_HTML])
        return [bytes(body, encoding=ENCODING)]


if __name__ == '__main__':
    print(__name__)
