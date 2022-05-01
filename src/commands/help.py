from colorama import Fore


def command_help(cli):
    cli.print("Usage: ")
    cli.println("ksa.exe [arguments]", Fore.RED)
    cli.println("")
    cli.println("Available arguments:")

    cli.print("   /n", Fore.YELLOW)
    cli.println("        -   prints all project members")

    cli.print("   /csvimp", Fore.YELLOW)
    cli.println("   -   imports all csv files from the current directory")

    cli.print("   /xmlimp", Fore.YELLOW)
    cli.println("   -   imports all xml files from the current directory")

    cli.print("   /jsonimp", Fore.YELLOW)
    cli.println("  -   imports all json files from the current directory")

    cli.print("   /etk", Fore.YELLOW)
    cli.println("      -   exports all labels to pdf files")
