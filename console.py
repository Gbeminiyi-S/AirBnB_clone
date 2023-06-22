#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the entry point of the command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exits the program with EOF
        """
        return True

    def emptyline(self):
        """Defines what happens when the `Enter` key is pressed
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
