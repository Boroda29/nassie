def parse_input_data(data: str):
    result = {}
    if data:
        # делим параметры через &
        params = data.split('&')
        for item in params:
            # делим ключ и значение через =
            k, v = item.split('=')
            result[k] = v
    return result


def application(environ, start_response):
    """
    :param environ: словарь данных от сервера
    :param start_response: функция для ответа серверу
    """
    # получаем параметры запроса
    query_string = environ['QUERY_STRING']
    print(query_string)
    # превращаем параметры в словарь
    request_params = parse_input_data(query_string)
    print(request_params)
    start_response('200 OK', [('Content-Type', 'text/html')])

    return [b'Hello world from a simple WSGI application!']

# gunicorn
# pip install gunicorn
# gunicorn simple_wsgi:application

# uwsgi
# pip install uwsgi
# uwsgi --http :8000 --wsgi-file simple_wsgi.py
