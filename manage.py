import os
import sys

from wsgi import Application
from nassie.core.management import execute

def application(environ, start_response):
    app = Application(environ)
    return app.call_as(start_response)


def execute_from_command_line(argv):
    execute(argv)


if __name__ == '__main__':
    execute_from_command_line(sys.argv)


