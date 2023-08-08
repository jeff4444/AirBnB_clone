#!/usr/bin/python3
"""AirBnB console"""


import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        sys.exit(0)

    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_create(self, arg):
        """Creates a new instance of BaseModel and saves it"""
        if arg:
            if arg == 'BaseModel':
                my_instance = models.base_model.BaseModel()
                my_instance.save()
                print(my_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
