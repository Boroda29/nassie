####Запуск приложения
```sh
$ gunicorn manage:application
$ uwsgi --http :8000 --wsgi-file manage:application
```

####Команды управления
```sh
$ python manage.py startapp имяпроекта
```

####Задания
    Добавил фабрику создания шаблонов модуль nassie\templator
    Добавил декоратор nassie\decors review_request() для отслеживания request
    Добавил декоратор nassie\decors fill_request() для предварительного заполнения request данными из View
    

####Вопросы и комментарии
* я что-то не понял декораторов класса
    

####Описание
| Модуль | Описание |
| ------ | ------ |
| manage.py | модуль управления проектом |
| wsgi.py | главный wsgi проекта |
| settngs.py | настройки проекта |

    
####Эмоции
    очень интересно, хочеться еще сильнее погрузиться
    СПАСИБО!