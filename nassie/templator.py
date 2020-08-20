import abc
from nassie.core.type_templators import HTML, App


class TemplatorFactory(abc.ABC):
    @staticmethod
    def create(network_name):
        NETWORKS = {
            'HTML': HtmlFactory,
            'APP': AppFactory
        }
        return NETWORKS[network_name]()

    @abc.abstractmethod
    def get(self):
        pass


class HtmlFactory(TemplatorFactory):
    def get(self):
        return HTML()

class AppFactory(TemplatorFactory):
    def get(self):
        return App()


if __name__ == '__main__':
    from apps.main.pages import Index
    from nassie.controllers.pages import Error404
    factory = TemplatorFactory.create("HTML").get()
    template = factory.render(Error404(), content={"title": "Главная"})
    print(template)
