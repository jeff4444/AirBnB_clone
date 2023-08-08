#!/usr/bin/python3
"""AirBnB console"""


import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit(0)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
