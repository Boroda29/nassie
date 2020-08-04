from nassie.consts import *
from nassie.common import templator


# Todo Доделать возвращение POST в отдельную функцию. пока сделать там просто Print
# TODO Сделать на абстрактных классах
class Index:
    def __init__(self):
        self.name_template = "index.html"

    def __call__(self, request):
        request['TITLE'] = "Главная"
        request['PAGE'] = self.name_template
        request['DATA_CONTENT'] = None
        body = templator.render(self.name_template, content=request)
        return STATUS_CODE["200"], body

class About:
    def __init__(self):
        self.name_template = "about.html"

    def __call__(self, request):
        request['TITLE'] = "Обо мне"
        request['PAGE'] = self.name_template
        request['DATA_CONTENT'] = {'name': "Александр", "tg": "@sanboroda"}
        body = templator.render(self.name_template, content=request)
        return STATUS_CODE["200"], body

class Form:
    def __init__(self):
        self.name_template = "form.html"

    def __call__(self, request):
        request['TITLE'] = "Тест формы отправки"
        request['PAGE'] = self.name_template
        request['DATA_CONTENT'] = None
        body = templator.render(self.name_template, content=request)
        return STATUS_CODE["200"], body

