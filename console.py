#!/usr/bin/python3
"""AirBNB clone console"""
import cmd
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

MODELS = [BaseModel, User, Amenity, Place, City, Review, State]


class HBNBCommand(cmd.Cmd):
    """Implementation of a AirBNB CLI"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates an instance from the valid model argument"""
        classnames = [cl.__name__ for cl in MODELS]
        args = self.parse(args)
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in classnames:
            print("** class doesn't exist **")
        else:
            for cl in MODELS:
                if args[0] == cl.__name__:
                    obj = cl()
                    obj.save()
                    print(obj.id)
                    return

    def do_show(self, line):
        """Show the string repr of an object having the given id"""
        args = self.parse(line)
        all_objs = models.storage.all()
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in [cl.__name__ for cl in MODELS]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing ** ")
        else:
            for k, v in all_objs.items():
                if args[1] == k.split(".")[1]:
                    print(v)
                    return
            print("** no instance found **")

    def do_destroy(self, line):
        """Destroy an object having the given id"""
        args = self.parse(line)
        all_objs = models.storage.all().copy()
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in [cl.__name__ for cl in MODELS]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing ** ")
        else:
            for k, v in all_objs.items():
                if args[1] == k.split(".")[1]:
                    models.storage.all().pop(k)
                    models.storage.save()
                    return
            print("** no instance found **")

    def do_all(self, line):
        """Prints all the instances of a Model"""
        args = self.parse(line)
        all_objs = models.storage.all().copy()
        if args[0] not in [cl.__name__ for cl in MODELS]:
            print("** class doesn't exist **")
        else:
            print(
                [str(value)
                 for key, value in all_objs.items()
                 if key.split(".")[0] == args[0]]
            )

    def do_update(self, line):
        """Updates the value of the entered model instance's attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"""
        args = self.parse(line)
        id_exists = False
        should_continue = False
        all_objs = models.storage.all()
        if args[0] == '':
            print("** class name missing **")
        elif args[0] not in [cl.__name__ for cl in MODELS]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing ** ")
        else:
            for k, v in all_objs.items():
                if args[1] == k.split(".")[1]:
                    obj = v
                    id_exists = True
                    should_continue = True
                    break
            if not id_exists:
                print("** no instance found **")
        if not should_continue:
            return
        if len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            setattr(obj, args[2], eval(args[3]))
            obj.save()

    def do_EOF(self, line):
        """exit console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        """Ensures the non-execution of anything when nothing is entered"""
        pass

    def parse(self, line):
        """Parses a line into a list of arguments"""
        return line.split(" ")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
