from nassie.constants import *
from nassie.controllers.pages import View
from apps.students.models import Students
import settngs

class Student(View):
    def __init__(self):
        super().__init__()
        self.name_template = "students.html"
        self.namespace = "students"
        self.title = "Студенты"
        self.model = Students

    def view_as(self, request):
        request = self.write_in_request(request)
        content_data = {"courses": settngs.DATA_BASE["courses"],
                        "students": settngs.DATA_BASE["students"]}

        if request['request_method'] == 'POST':
            self.method_post(request)
        request['content_data'] = content_data
        body = self.templator.render(self, content=request)
        return STATUS_CODE['200'], body

    def method_post(self, request):
        self.model(request['request_data']['firstname'],
                   request['request_data']['lastname'],
                   request['request_data']['course']).save()
