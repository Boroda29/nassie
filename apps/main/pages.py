from nassie.constants import *
from nassie.controllers.pages import View
from nassie.decors import fill_request


class Index(View):
    def __init__(self):
        super().__init__()
        self.name_template = "index.html"
        self.namespace = "main"
        self.title = "Главная"

    @fill_request
    def view_as(self, request):
        request['content_data'] = None
        body = self.templator.render(self, content=request)
        return STATUS_CODE['200'], body
