from nassie.models import Model

class Student(Model):
    _model_name_ = "students"

    def __init__(self, firstname, lastname, course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course


if __name__ == '__main__':
    from apps.course.models import Cours
    Student("python", "описание", Cours("python", "описание")).save()
    Student("java", "описание", Cours("java", "описание")).save()
