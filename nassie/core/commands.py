import os
from nassie.constants import BASE_DIR
from nassie.core.utils import exists_path
from nassie.templator import TemplatorFactory

def startapp(name_app):
    factory = TemplatorFactory.create("APP").get()
    packet_name_files = {"pages": "namespace",
                         "models": ""}
    path_error = False
    paths_pack = {
        "apps": os.path.join(BASE_DIR, "apps"),
        "ref": os.path.join(BASE_DIR, "nassie", "docs", "ref")
    }

    for path in paths_pack.values():
        if not exists_path(path):
            # todo сделать классы ошибок
            print(f"Ошибка создания пакета. Путь не найден: {path}")
            path_error = True

    paths_pack["new_app"] = os.path.join(BASE_DIR, "apps", name_app)
    paths_pack["templates_app"] = os.path.join(BASE_DIR, "apps", name_app, "templates")

    if not path_error:
        if not os.path.exists(paths_pack["new_app"]):
            os.mkdir(paths_pack["new_app"])

        if not os.path.exists(paths_pack["templates_app"]):
            os.mkdir(paths_pack["templates_app"])

        file_init = open(os.path.join(paths_pack["new_app"], f"__init__.py"), 'w', encoding='utf-8')
        file_init.close()

        file_html = open(os.path.join(paths_pack["templates_app"], f"{name_app}.html"), 'w', encoding='utf-8')
        file_html.close()

        for file_name, field in packet_name_files.items():
            path_file_template = os.path.join(paths_pack["ref"], f"{file_name}.txt")
            if not exists_path(path_file_template):
                # todo сделать классы ошибок файла
                print(f"Шаблон не найден: {path_file_template}")
                break

            path_file_new = os.path.join(paths_pack["new_app"], f"{file_name}.py")
            file_page = open(path_file_new, 'w', encoding='utf-8')
            file_page.write(factory.render(file_name, name_app=name_app))
            file_page.close()

def help_cmd(option):
    file_help = open(os.path.join(BASE_DIR, "nassie", "docs", "ref", "help.txt"), "r", encoding="utf-8")
    text_help = file_help.read()
    file_help.close()
    print(text_help)


if __name__ == '__main__':
    help_cmd()
