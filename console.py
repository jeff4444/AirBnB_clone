#!/usr/bin/python3
"""AirBnB console"""


import cmd
import models


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of a class and saves it"""
        if arg:
            args_list = arg.split()
            class_dicts = {'BaseModel': models.base_model.BaseModel,
                           'User': models.user.User,
                           'Place': models.place.Place,
                           'Review': models.review.Review,
                           'City': models.city.City,
                           'Amenity': models.amenity.Amenity,
                           'State': models.state.State,
                           }
            my_instance = None
            for key in class_dicts:
                if args_list[0] == key:
                    my_instance = class_dicts[key]()
            if my_instance is not None:
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
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
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
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
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

    def do_all_list(self, arg):
        """return all instances of a certain class or simply all instances"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
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
        return all_list

    def do_all(self, arg):
        """Print all instances of a certain class"""
        print(self.do_all_list(arg))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if arg:
            args_list = arg.split()
            available_classes = ['BaseModel', 'User', 'Place',
                                 'City', 'Amenity', 'Review', 'State']
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
                if args_list[3][0] == "'" or args_list[3][0] == '"':
                    args_list[3] = args_list[3][1:(len(args_list[3]) - 1)]
                setattr(models.storage.all()[key_name], str(args_list[2]),
                        str(args_list[3]))
                models.storage.save()
        else:
            print("** class name missing **")

    def default(self, arg):
        args = arg.split()
        commands_list = args[0].split('.')
        if len(commands_list) == 1:
            return
        func = commands_list[1]
        if func == 'all()':
            self.do_all(commands_list[0])
        elif func == 'count()':
            print(len(self.do_all_list(commands_list[0])))
        elif func[0:4] == 'show':
            arg = commands_list[0] + ' ' + func[6:-2]
            self.do_show(arg)
        elif func[0:7] == 'destroy':
            arg = commands_list[0] + ' ' + func[9:-2]
            self.do_destroy(arg)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
