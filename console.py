#!/usr/bin/env python3
"""ontains the entry point of the command interpreter"""
from ast import arg
import cmd
from models.base_model import BaseModel
import models
from models import storage
import json
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


"""from models.base_model import BaseModel"""
list_class = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
              "City": City, "Place": Place, "Review": Review, "State": State}


class HBNBCommand(cmd.Cmd):
    """star prompt"""
    prompt = "(hbnb) "

    def emptyline(self):
        "reset if are a emptyline"
        pass

    def do_quit(self, arg):
        """exit to shell"""
        exit()

    def do_EOF(self, arg):
        """exit to file"""
        exit()

    def help_quit(self):
        """info of quit"""
        print("Quit command to exit the program")

    def help_EOF(self):
        """info of EOF"""
        print("end of file")

    def do_create(self, arg):
        """create - create method"""
        arg = arg.split()
        if len(arg) == 0:
            print("** class name missing **")
            return False
        elif arg[0] in list_class:
            new_object = list_class[arg[0]]()
        else:
            print("** class doesn't exist **")
            return
        print(new_object.id)
        new_object.save()

    def do_show(self, arg):
        """deploy all"""
        arg = arg.split()
        all_objs = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg[0] not in list_class:
            print("** class doesn't exist **")
            return
        elif len(arg) == 1:
            print("** instance id missing **")
            return
        elif f'{arg[0]}.{arg[1]}' in all_objs.keys():
            print(all_objs[f"{arg[0]}.{arg[1]}"])
            return
        else:
            print("** no instance found **")
            
    def do_destroy(self, args):
        """Destroy an object"""
        arg = arg.split()
        if len(args) == 0:
            print("** class name missing **")

        elif arg[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        else:
            data = storage.all()
            save2 = arg[0] + '.' + arg[1]
            no_instance = False
            for key in data.copy().keys():
                if save2 in key:
                    del data[str(save2)]
                    storage.save()
                    no_instance = True
            if not no_instance:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances"""
        all_objs = models.storage.all()
        instances = []
        if not arg:
            for obj in all_objs.values():
                instances.append(obj.__str__())
            print(f"{instances}")
        else:
            if arg not in list_class:
                print("** class doesn't exist **")
                return
            else:
                for obj, value in all_objs.items():
                    if arg == value.to_dict()["__class__"]:
                        instances.append(value.__str__())
        print(instances)
        
    def do_update(self, arg):
        """Update an object"""

        if len(arg) == 0:
            print("** class name missing **")
            return
        splitted_args = arg.split()
        if splitted_args[0] not in list_class:
            print("** class doesn't exist **")
            return
        if len(splitted_args) == 1:
            print("** instance id missing **")
            return
        recuento = storage.all()
        key_compare = "{}.{}".format(splitted_args[0], splitted_args[1])
        if key_compare in recuento.keys():
            if len(splitted_args) == 2:
                print("** attribute name missing **")
                return
            if len(splitted_args) == 3:
                print("** value missing **")
                return
            setattr(recuento[key_compare], splitted_args[2], splitted_args[3])
            storage.save()
        else:
            print("** no instance found **")
            return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
