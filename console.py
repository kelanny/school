#!/usr/bin/env python3
""" Console module """

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class for the HBNB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Overrides the default behavior of repeating the last command when an empty line is entered.
        """
        pass

    def do_help(self, arg):
        """
        Provides help for commands.
        """
        if arg:
            # If specific command help is requested, call default help
            return super().do_help(arg)
        else:
            print("Documented commands (type help <topic>):")
            print("========================================")
            print("EOF   quit   help")
            print("\nType 'help <command>' to see more details about a specific command.")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
