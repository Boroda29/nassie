import datetime

def time_call(request, **kwargs):
    request['time_call'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
