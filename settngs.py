from controllers.pages import Index, About, Form
from controllers.fronts import *

ROUTES = {
    "/": Index(),
    "/index": Index(),
    "/about": About(),
    "/form": Form()
}

FRONTS = [
    time_call,
    add_title,
    add_page,
    get_method_data_request
]
