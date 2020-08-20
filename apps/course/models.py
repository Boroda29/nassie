from nassie.models import Model

class Cours(Model):
    _model_name_ = "courses"

    def __init__(self, name, title):
        self.name = name
        self.title = title


if __name__ == '__main__':
    Cours("python", "описание").save()
    Cours("java", "описание").save()
