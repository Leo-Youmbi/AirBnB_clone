#!/usr/bin/python3
"""AirBNB clone console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Implementation of a AirBNB CLI"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self) -> bool:
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
