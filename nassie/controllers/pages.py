import abc
from nassie.constants import STATUS_CODE
from nassie.templator import TemplatorFactory


class View(abc.ABC):
    def __init__(self):
        self.templator = TemplatorFactory.create("HTML").get()
        self.page = None
        self.namespace = None
        self.title = None
        self.model = None

    def write_in_request(self, request: dict):
        for key, value in self.__dict__.items():
            if key in request:
                request[key] = value
        return request

    @abc.abstractmethod
    def view_as(self, request):
        pass

    def method_get(self, request):
        print(request['request_method'])

    def method_post(self, request):
        print(request['request_method'])
        print(request['request_data'])


class Error404(View):
    def __init__(self):
        super().__init__()
        self.name_template = "404.html"
        self.namespace = "404"
        self.title = "404"

    def view_as(self, request):
        request = self.write_in_request(request)
        body = self.templator.render(self, content=request)
        return STATUS_CODE["404"], body


