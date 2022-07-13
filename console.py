#!/usr/bin/env python3

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
list_class = ["BaseModel"]


class HBNBCommand(cmd.Cmd):
    """star prompt"""
    prompt = "(hbnb) "

    def emptyline(self):
        "reset if are a emptyline"
        pass

    def do_quit(self, arg):
        exit()

    def do_EOF(self, arg):
        exit()

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("end of file")

    def do_create(self, arg):
        if arg in list_class:
            str_class = "{}()".format(arg)
            new_object = eval(str_class)
            print(new_object.id)
        elif len(arg) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """comments"""
        arg = arg.split()
        temp_list = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return

        elif temp_list[0] not in list_class:
            print("** class doesn't exist **")
            return
        if not temp_list[1] or len(temp_list[1]) == 0:
            print("** instance id missing **")
        elif f'{arg[0]}.{arg[1]}' in temp_list.keys():
            print(temp_list[f"{arg[0]}.{arg[1]}"])
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
        """Print all objects"""
        new_token = arg.split()
        diccionario = models.storage.all()
        if len(arg) == 0:
            print("** class name missing **")
            return
        if not arg or new_token[0] in HBNBCommand.classes:
            concatenar = []
            for iterador in diccionario.values():
                concatenar.append(iterador())
                print(concatenar)
        else:
            print("** class doesn't exist **")

    def do_update(self, args):
        """Update an object"""

        if len(args) == 0:
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
