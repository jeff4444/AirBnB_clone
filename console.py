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
        """Creates a new instance of a class and saves it"""
        if arg:
            args_list = arg.split()
            if args_list[0] == 'BaseModel':
                my_instance = models.base_model.BaseModel()
            elif args_list[0] == 'User':
                my_instance = models.user.User()
            elif args_list[0] == 'Place':
                my_instance = models.place.Place()
            elif args_list[0] == 'State':
                my_instance = models.state.State()
            elif args_list[0] == 'City':
                my_instance = models.city.City()
            elif args_list[0] == 'Review':
                my_instance = models.review.Review()
            elif args_list[0] == 'Amenity':
                my_instance = models.amenity.Amenity()
            else:
                print("** class doesn't exist **")
                return
            my_instance.save()
            print(my_instane.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Shows an instance using its ID"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
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
            available_classes = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
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
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
            if arg not in available_classes:
                print("** class doesn't exist **")
                return
            all_list = []
            for key, val in models.storage.all().items():
                if arg == key[0:len(args_list[0])]:
                    all_list.append(str(val))
        else:
            all_list = []
            for key, val in models.storage.all().items():
                all_list.append(str(val))
        print(all_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place', 'City', 'Amenity', 'Review', 'State']
            if args_list[0] not in available_classes:
                print("** class doesn't exist **")
                return
            if len(args_list) == 1:
                print("** instance id missing **")
                return
            key_name = f'{args_list[0]}.{args_list[1]}'
            if key_name not in models.storage.all():
                print("** no instance found **")
            elif len(args_list) == 2:
                print("** attribute name missing **")
            elif len(args_list) == 3:
                print("** value missing **")
            else:
                models.storage.all()[key_name][args_list[2]] = args_list[3]
                models.storage.save()
        else:
            print("** class name missing **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
