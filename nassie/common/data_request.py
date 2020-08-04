from nassie.consts import CONTENT_TYPE_APP_FORM, CONTENT_TYPE_FORM_DATA
import quopri

# TODO перенести в основной фреимворк
class DataRequest:
    def __init__(self, environ):
        self.environ = environ
        self.method = environ['REQUEST_METHOD']
        self.content_type = ""

    def _parse_get_post_app_form(self):
        result = {}
        if self.data:
            # делим параметры через &
            params = self.data.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = self.decode_value(v)
        return result

    def _parse_get_post_form_data(self):
        result = {}
        if self.data:
            pass
        return result

    def _get_data_requestGET(self):
        self.data = self.environ['QUERY_STRING']
        return self._parse_get_post_app_form()

    def _get_data_requestPOST(self):
        result = {}
        self.content_type = self.environ.get('CONTENT_TYPE')
        content_length_data = self.environ.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0

        if content_length > 0:
            data = self.environ['wsgi.input'].read(content_length)
        else:
            return result

        self.data = data.decode(encoding='utf-8')
        if CONTENT_TYPE_APP_FORM[1] in self.content_type:
            result = self._parse_get_post_app_form()
        if CONTENT_TYPE_FORM_DATA[1] in self.content_type:
            result = self._parse_get_post_form_data()
        return result

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        val_decode_str = quopri.decodestring(val_b)
        return val_decode_str.decode('UTF-8')

    def get_data_request(self):
        if self.method == "GET":
            return self._get_data_requestGET()
        if self.method == "POST":
            return self._get_data_requestPOST()

