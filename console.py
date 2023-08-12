#!/usr/bin/python3
"""AirBNB clone console"""
import cmd

from models.base_model import BaseModel

MODELS = [BaseModel]


class HBNBCommand(cmd.Cmd):
    """Implementation of a AirBNB CLI"""
    prompt = "(hbnb) "

    def do_create(self, args):
        """Creates an instance from the valid model argument"""
        classnames = [cl.__name__ for cl in MODELS]
        args = self.parse(args)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classnames:
            print("** class doesn't exist **")
        else:
            for cl in MODELS:
                if args[0] == cl.__name__:
                    obj = cl()
                    obj.save()
                    print(obj.id)

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
