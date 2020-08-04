from nassie.common.data_request import DataRequest
import datetime

def time_call(request, **kwargs):
    request['TIME_CALL'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def add_title(request, **kwargs):
    request['TITLE'] = 'Name page'

def add_page(request, **kwargs):
    request['PAGE'] = None

def add_content(request, **kwargs):
    request['DATA_CONTENT'] = None

# TODO перенести в основной фреимворк
def get_method_data_request(request, **kwargs):
    request['METHOD'] = None
    request['DATA_REQUEST'] = None

    if kwargs.get('env'):
        dr = DataRequest(kwargs['env'])
        request['METHOD'] = dr.method
        request['DATA_REQUEST'] = dr.get_data_request()

