from controllers.fronts import *
from apps.main.pages import Index
from apps.about.pages import About
from apps.sender_form.pages import Form
from apps.course.pages import Course
from apps.students.pages import Students


ROUTES = {
    "/": Index(),
    "/index": Index(),
    "/about": About(),
    "/form": Form(),
    "/course": Course(),
    "/students": Students()
}

FRONTS = [
    time_call
]

DATA_BASE = {"courses": [],
             "students": []}

