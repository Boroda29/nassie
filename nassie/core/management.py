from nassie.core.commands import startapp

commands = {
    "startapp": startapp
}

def execute(argv):
    try:
        subcommand = argv[1]
    except IndexError:
        subcommand = 'help'

    try:
        options = argv[2]
    except IndexError:
        options = 'help'

    if subcommand and options:
        if subcommand in commands:
            commands[subcommand](options)
    else:
        pass
