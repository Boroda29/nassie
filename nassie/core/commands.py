import os

from nassie.constants import BASE_DIR
from nassie.core.utils import exists_path

def startapp(name_app):
    packet_name_files = {"pages": "namespace"}
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

        for file_name, field in packet_name_files.items():
            path_file_template = os.path.join(paths_pack["ref"], f"{file_name}.txt")
            if not exists_path(path_file_template):
                # todo сделать классы ошибок файла
                print(f"Шаблон не найден: {path_file_template}")
                break

            path_file_new = os.path.join(paths_pack["new_app"], f"{file_name}.py")

            file_template = open(path_file_template, 'r', encoding='utf-8')
            file_page = open(path_file_new, 'w', encoding='utf-8')
            with file_template as f:
                file_page.write(f.read().replace(f":{field}:", name_app))
            file_page.close()
            file_template.close()


if __name__ == '__main__':
    startapp("test")
