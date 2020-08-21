from nassie.core.commands import startapp, help_cmd

commands = {
    "startapp": startapp,
    "help": help_cmd
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
            help_cmd()
    else:
        help_cmd()


if __name__ == '__main__':
    execute(["help"])
