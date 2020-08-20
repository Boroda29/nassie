from nassie.models import Model

class Students(Model):
    def __init__(self, firstname, lastname, course):
        self.firstname = firstname
        self.lastname = lastname
        self.course = course


if __name__ == '__main__':
    from apps.course.models import Courses
    Students("python", "описание", Courses("python", "описание")).save()
    Students("java", "описание", Courses("java", "описание")).save()
