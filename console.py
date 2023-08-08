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

    def do_show(self, arg):
        """Shows an instance using its ID"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key_name])
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """Destroys an instance using its ID"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key_name]
                models.storage.save()
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """Print all instances of a certain class or simply all instances"""
        if arg:
            available_classes = ['BaseModel']
            if arg not in available_classes:
                print("** class doesn't exist **")
                return
            all_list = []
            for key, val in models.storage.all().items():
                if arg == key[0:len(arg)]:
                    all_list.append(str(val))
        else:
            all_list = []
            for key, val in models.storage.all().items():
                all_list.append(str(val))
        print(all_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
