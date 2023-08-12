#!/usr/bin/python3
"""AirBNB clone console"""
import cmd
import models

from models.base_model import BaseModel

MODELS = [BaseModel]


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
                    break

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

    def do_EOF(self, line):
        """exit console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        pass

    def parse(self, line):
        args = line.split(" ")
        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
