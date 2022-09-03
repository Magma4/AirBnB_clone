#!/usr/bin/python3
"""this is the console for AirBnB"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """this class defines a console object
    """
    prompt = '(hbnb)'

    def do_quit(self, *args):
        """quits the interpreter"""
        return True

    def do_EOF(self, obj):
        """EOF exits the program"""
        print()
        return True

    def emptyline(self):
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
