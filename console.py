#!/usr/bin/env python3

import cmd, sys, os
import json
import shlex
"""from models.base_model import BaseModel"""

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
        
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()