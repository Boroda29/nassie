import os
import abc
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from nassie.constants import BASE_DIR


class TemplatorType(abc.ABC):
    @abc.abstractmethod
    def render(self, page, **kwargs):
        pass

class HTML(TemplatorType):
    def render(self, page, **kwargs):
        if page.namespace == "404":
            path_loader = os.path.join(BASE_DIR, "templates")
        else:
            path_loader = os.path.join(BASE_DIR, "apps", page.namespace, "templates")

        file_loader = FileSystemLoader(path_loader)
        env = Environment(loader=file_loader)

        template = env.get_template(page.name_template)
        return template.render(**kwargs)


class App(TemplatorType):
    def render(self, template_name, **kwargs):
        env = Environment()
        folder = os.path.join(BASE_DIR, "nassie", "docs", "ref")
        env.loader = FileSystemLoader(folder)
        template = env.get_template("pages.txt")

        file = template.render(content={"name": f"{template_name.title()}",
                                        "namespace": f"{template_name}"})
        return file
