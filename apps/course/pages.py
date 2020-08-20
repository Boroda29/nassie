from nassie.constants import *
from nassie.controllers.pages import View
from apps.course.models import Cours
import settngs

class Course(View):
    def __init__(self):
        super().__init__()
        self.name_template = "course.html"
        self.namespace = "course"
        self.title = "Курсы"
        self.model = Cours

    def view_as(self, request):
        request = self.write_in_request(request)
        if request['request_method'] == 'POST':
            self.method_post(request)
        request['content_data'] = settngs.DATA_BASE['courses']
        body = self.templator.render(self, content=request)
        return STATUS_CODE['200'], body

    def method_post(self, request):
        self.model(request['request_data']['name'], request['request_data']['title']).save()
