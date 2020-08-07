from controllers.fronts import *
from apps.main.pages import Index
from apps.about.pages import About
from apps.sender_form.pages import Form


ROUTES = {
    "/": Index(),
    "/index": Index(),
    "/about": About(),
    "/form": Form()
}

FRONTS = [
    time_call
]


