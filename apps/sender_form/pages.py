from nassie.constants import *
from nassie import templator
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
        body = templator.render(self.name_template, self.namespace, content=request)
        if request['request_method'] == 'POST':
            self.method_post(request)
            body = templator.render(Index().name_template, Index().namespace, content=request)
        return STATUS_CODE['200'], body