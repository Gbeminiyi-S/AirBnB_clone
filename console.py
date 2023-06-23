#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd
from models.base_model import BaseModel
from models import storage

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

    def do_show(self, args):
        """Prints the string representation of an instance based on the
            class name and id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f'{args[0]}.{args[1]}'
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance_key])

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_key = f'{args[0]}.{args[1]}'
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                del(storage.all()[instance_key])
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
