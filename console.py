#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd
from models.base_model import BaseModel

classes = ["BaseModel"]

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

    def do_create(self, args):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """ 
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
