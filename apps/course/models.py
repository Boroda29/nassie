from nassie.models import Model

class Courses(Model):
    def __init__(self, name, title):
        self.name = name
        self.title = title


if __name__ == '__main__':
    Courses("python", "описание").save()
    Courses("java", "описание").save()
