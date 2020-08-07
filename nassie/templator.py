import os
from jinja2 import Template
from jinja2 import FileSystemLoader
from jinja2.environment import Environment

from nassie.constants import BASE_DIR


def render(template_name, namespace, **kwargs):
    # path_templates = os.path.join(BASE_DIR, "apps", namespace, "templates", template_name)
    path_templates = template_name

    path_loader = os.path.join(BASE_DIR, "templates")
    file_loader = FileSystemLoader(path_loader)
    env = Environment(loader=file_loader)

    template = env.get_template(path_templates)
    return template.render(**kwargs)


if __name__ == '__main__':
    print(render("about.html", "about", content={"title": "Главная", 'content_data':{'name': "Александр", "tg": "@sanboroda"}}))
