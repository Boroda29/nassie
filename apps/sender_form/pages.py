from nassie.constants import *
from nassie.controllers.pages import View
from apps.main.pages import Index

class Form(View):
    def __init__(self):
        super().__init__()
        self.name_template = "form.html"
        self.namespace = "sender_form"
        self.title = "Тест форма отправки"

    def view_as(self, request):
        request = self.write_in_request(request)
        request['content_data'] = None
        body = self.templator.render(self, content=request)
        if request['request_method'] == 'POST':
            self.method_post(request)
            body = self.templator.render(Index(), content=request)
        return STATUS_CODE['200'], body