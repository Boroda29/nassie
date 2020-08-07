import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ENCODING = "utf-8"

CONTENT_TYPE_TEXT_HTML = ('Content-Type', 'text/html')
CONTENT_TYPE_TEXT_CSS = ('Content-Type', 'text/css')
CONTENT_TYPE_APP_JSON = ('Content-Type', 'application/json')
CONTENT_TYPE_FORM_DATA = ('Content-Type', 'multipart/form-data')
CONTENT_TYPE_APP_FORM = ('Content-Type', 'application/x-www-form-urlencoded')

STATUS_CODE = {
    "200": "200 OK",
    "404": "404 Not Found"
}

MAP_ENV_DATA_WSGI = {
    "REQUEST_METHOD": "REQUEST_METHOD",
    "QUERY_STRING": "QUERY_STRING",
    "CONTENT_TYPE": "CONTENT_TYPE",
    "CONTENT_LENGTH": "CONTENT_LENGTH",
    "PATH_INFO": "PATH_INFO",
    "wsgi.input": "WSGI_INPUT"
}

REQUEST_KEYS = (
    'title',
    'page',
    'namespace',
    'request_method',
    'request_data',
    'content_data'
)
