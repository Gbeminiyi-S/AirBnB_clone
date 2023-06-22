#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Defines the entry point of the command interpreter"""
    intro = "Welcome to the AirBnB Console"
    prompt = "(hbnb) "

    def do_quit(self):
        """Exits the program
        """
        exit()

    def do_EOF(self):
        """Exits the program
        """
        exit()

    def emptyline(self):
        """Defines what happens when the `Enter` key is pressed
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
