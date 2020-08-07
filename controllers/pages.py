from nassie.constants import *
from nassie import templator
from nassie.controllers.pages import View


class Index(View):
    def __init__(self):
        super().__init__()
        self.name_template = "index.html"
        self.namespace = "index"
        self.title = "Главная"

    def view_as(self, request):
        request = self.write_in_request(request)
        request['content_data'] = None
        body = templator.render(self.name_template, content=request)
        return STATUS_CODE['200'], body


class About(View):
    def __init__(self):
        super().__init__()
        self.name_template = "about.html"
        self.namespace = "about"
        self.title = "Обо мне"

    def view_as(self, request):
        request = self.write_in_request(request)
        request['content_data'] = {'name': "Александр", "tg": "@sanboroda"}
        body = templator.render(self.name_template, content=request)
        return STATUS_CODE['200'], body


class Form(View):
    def __init__(self):
        super().__init__()
        self.name_template = "form.html"
        self.namespace = "form"
        self.title = "Тест форма отправки"

    def view_as(self, request):
        request = self.write_in_request(request)
        request['content_data'] = None
        body = templator.render(self.name_template, content=request)
        if request['request_method'] == 'POST':
            self.method_post(request)
            body = templator.render(Index().name_template, content=request)
        return STATUS_CODE['200'], body
