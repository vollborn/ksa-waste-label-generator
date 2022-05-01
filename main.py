import inspect
import sys

from src.commands.csvimp import command_csvimp
from src.commands.etk import command_etk
from src.commands.help import command_help
from src.commands.jsonimp import command_jsonimp
from src.commands.n import command_n
from src.commands.xmlimp import command_xmlimp
from src.services.CLI import CLI
from src.services.Config import Config


def main():
    args = sys.argv

    dependencies = {
        "args": args,
        "cli": CLI(),
        "config": Config()
    }

    if len(args) < 2:
        inject(command_help, dependencies)
        return

    command = args[1]
    function = command_help

    if command == "/n":
        function = command_n
    elif command == "/csvimp":
        function = command_csvimp
    elif command == "/jsonimp":
        function = command_jsonimp
    elif command == "/xmlimp":
        function = command_xmlimp
    elif command == "/etk":
        function = command_etk

    inject(function, dependencies)


def inject(function, dependencies):
    argSpecs = inspect.getfullargspec(function)
    args = []

    dependencyKeys = dependencies.keys()

    for argName in argSpecs.args:
        if argName not in dependencyKeys:
            raise Exception("Dependency \"" + argName + "\" not found.")

        args.append(dependencies[argName])

    function(*args)


if __name__ == "__main__":
    main()
