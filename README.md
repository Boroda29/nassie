####Запуск приложения
```sh
$ gunicorn manage:application
$ uwsgi --http :8000 --wsgi-file manage:application
```

####Задания
    Все задания выполнены
    

####Вопросы и комментарии
* пусто
    

####Описание
| Модуль | Описание |
| ------ | ------ |
| manage.py | запуск приложения и передача environ |
| wsgi.py | главный wsgi проекта |
| settngs.py | настройки проекта |
| templator.py | рендер шаблона из pages.py |
| controllers.fronts.py | front контроллеры |
| controllers.pages.py | page контроллеры |
| common.consts.py | константы |
| common.data_request.py | получение данных из GET или POST запроса |
    
####Эмоции
    очень интересно, хочеться еще сильнее погрузиться
    СПАСИБО!