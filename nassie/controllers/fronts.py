from nassie.data_request import DataRequest
from nassie.constants import REQUEST_KEYS

class FrontControllerApp:
    @staticmethod
    def add_attr_pages(request, **kwargs):
        for _ in REQUEST_KEYS:
            request[_] = None

    @staticmethod
    def get_method_data_request(request, **kwargs):
        if kwargs.get('env'):
            dr = DataRequest(kwargs['env'])
            request['request_method'] = dr.method
            request['request_data'] = dr.get_data_request()


if __name__ == '__main__':
    print(__name__)
