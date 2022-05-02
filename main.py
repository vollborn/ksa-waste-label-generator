import inspect
import sys

from src.commands.csvimp import command_csvimp
from src.commands.etk import command_etk
from src.commands.help import command_help
from src.commands.jsonimp import command_jsonimp
from src.commands.n import command_n
from src.commands.xmlimp import command_xmlimp
from src.services.DependencyInjector import DependencyInjector


def main():
    args = sys.argv

    if len(args) < 2:
        DependencyInjector.inject(command_help)
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

    DependencyInjector.inject(function)


if __name__ == "__main__":
    main()
