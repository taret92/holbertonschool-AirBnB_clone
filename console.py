#!/usr/bin/env python3

import cmd, sys, os
from hashlib import new
from logging import logMultiprocessing
from re import template
from posixpath import split
from models.engine import storage 
import json
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


"""from models.base_model import BaseModel"""
list_class = ["BaseModel"]

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    
    def emptyline(self):
        "reset if are a emptyline"
        pass
    def do_quit(self, args):
        exit()
    def do_EOF(self, args):
        exit()
    def help_quit(self):
        print("Quit command to exit the program")
    def help_EOF(self):
        print("end of file")
    def do_create(self, args):
        if args in list_class:
            str_class = "{}()".format(args)
            new_object = eval(str_class)
            print(new_object.id)
        elif len(args) == 0:
            print("** class name missing **")
        else:
            print("** class doesn't exist **")
    def do_show(self, args):
        """comentario"""
        if len(args) == 0:
            print("** class name missing **")
            return
        temp_list = args.split(" ")
        if temp_list[0] not in list_class:
            print("** class doesn't exist **")
            return
        if not temp_list[1] or len(temp_list[1]) == 0:
            print("** instance id missing **")
        str_class_id = "{}.{}".format(temp_list[0], temp_list[1])
        tmp_objects = storage.all()
        if str_class_id in tmp_objects.keys():
            print(tmp_objects[str_class_id])
        else:
            print("** no instance found **")
            return
    def do_destroy(self, args):
        """Destroy an objects"""

        if len(args) == 0:
            print("** class name missing **")
            return
        new_list = shlex.split(args)
        if new_list[0] not in list_class:
            print("** class doesn't exist **")
            return
        if len(new_list) <= 1:
            print("** instance id missing **")
            return
        new_str = "{}.{}".format(new_list[0], new_list[1])
        diccionario = storage.all()
        if new_str in diccionario.keys():
            diccionario.pop(new_str)
            storage.save()
        else:
            print("** no instance found **")
    def do_all(self, args):
        """Print all objects"""
        new_token = args.split()
        diccionario = storage.all()
        if len(args) == 0:
            print("** class name missing **")
            return
        if not args or new_token[0] in HBNBCommand.classes:
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
        splitted_args = shlex.split(args)
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
