#!/usr/bin/python3
"""This module defines the class `HBHBCommand`"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]


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

    def do_all(self, args):
        """Prints all string representation of all instances based or
            not on the class name
        """
        args = args.split()
        if len(args) == 0:
            for obj in storage.all().values():
                print(obj)
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            for key in storage.all():
                if key.startswith(args[0]):
                    print(storage.all()[key])

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            instance_key = f'{args[0]}.{args[1]}'
            if instance_key not in storage.all():
                print("** no instance found **")
            else:
                obj = storage.all()[instance_key]
                setattr(obj, args[2], eval(args[3]))
                obj.save()

    def default(self, arg):
        "Defines any other command"
        args = arg.split('.')
        if args[0] in classes:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                count = 0
                for key in storage.all():
                    if key.startswith(args[0]):
                        count += 1
                print(count)
            elif args[1].startswith("show"):
                uuid = eval(args[1].strip("show()"))
                self.do_show(f"{args[0]} {uuid}";)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
