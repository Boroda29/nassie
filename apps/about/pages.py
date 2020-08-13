from nassie.constants import *
from nassie.controllers.pages import View

class About(View):
    def __init__(self):
        super().__init__()
        self.name_template = "about.html"
        self.namespace = "about"
        self.title = "Обо мне"

    def view_as(self, request):
        request = self.write_in_request(request)
        request['content_data'] = {'name': "Александр", "tg": "@sanboroda"}
        body = self.templator.render(self, content=request)
        return STATUS_CODE['200'], body
