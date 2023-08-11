#!/usr/bin/python3
"""AirBNB clone console"""
import cmd


class AirbnbShell(cmd.Cmd):
    """Implementation of a AirBNB CLI"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit console on EOF signal (^D)"""
        return True

    def do_quit(self, line):
        """exit console"""
        return True


if __name__ == '__main__':
    AirbnbShell().cmdloop()
