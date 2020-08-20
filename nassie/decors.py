import datetime

def review_request(func):
    def inner(*args, **kwargs):
        print(f"Вызов {func.__name__} в {datetime.datetime.now()}")
        if len(args) == 2:
            print(f"request: {args[1]}")
        return func(*args, **kwargs)
    return inner

def fill_request(func):
    def inner(*args, **kwargs):
        if func.__name__ == "view_as" and len(args) == 2:
            self = args[0]
            request = args[1]
            request = self.write_in_request(request)
            return func(self, request)
        return func(*args, **kwargs)
    return inner
