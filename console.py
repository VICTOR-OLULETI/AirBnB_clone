#!/usr/bin/python3
"""This program is resposible for the cosole/interactive part of the hbnb"""


import cmd
from models import storage
from models.base_model import BaseModel

classes = {"BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    """Class definition for basic HBNB commands"""
    """ intro = 'Welcome to the HBNB console.
    Type help or ? to listcommands.\n'
    """
    prompt = '(hbnb) '

    # ----- basic HBNB commands -----
    def do_create(self, arg):
        args = arg.split()
        if args is None or len(args) == 0:
            print('** classs name missing **')
            return False
        if (args[0] in classes):
            Instance = classes[args[0]]()
            Instance.save()
        else:
            print("** class doesn't exist **")
            return False
        print(Instance.id)

    def do_show(self, arg):
        args = arg.split()
        if args is None or len(args) == 0:
            print("** class missing **")
            return False
        if (args[0] not in classes):
            print("** class doesn't exist **")
            return False
        if (len(args) == 1):
            print("** instance id missing **")
            return False
        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key not in all_objs:
                print("** no instance found **")
                return False
        else:
            print(all_objs[key])

    def do_update(self, arg):
        args = arg.split()
        all_objs = storage.all()
        if args is None or len(args) == 0:
            print("** class name missing **")
            return False
        if (args[0] not in classes):
            print("** class name missing **")
            return False
        if (len(args) == 1):
            print("** instance id missing **")
            return False
        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key not in all_objs:
            print("** no instance found **")
            return False
        if (len(args) == 2):
            print("** attribute name missing **")
            return False
        if (len(args) == 3):
            print("** value missing **")
        all_obj_key = all_objs[key]
        # all_obj_key[args[2]] = args[3]
        setattr(all_obj_key, args[2], args[3])
        all_obj_key.save()


    def do_destroy(self, arg):
        args = arg.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
            return False

        if (args[0] not in classes):
            print("**class doesn't exist **")
            return False

        if (args[1] is None):
            print("** instance id missing **")
            return False
        all_objs = storage.all()
        key = args[0] + '.' + args[1]
        if key not in all_objs:
            print(" no instance found **")
            return False
        else:
            Instance = classes[args[0]]()
            del all_objs[key]
            Instance.save()

    def do_all(self, arg):
        result = []
        args = arg.split()
        all_objs = storage.all()
        if (len(args) >= 1):
            if (args[0] not in classes):
                print("** class doesn't exist **")
                return False
        for obj_id in all_objs.keys():
            obj = all_objs[obj_id]
            result.append(str(obj))
        print(result)

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'Exit the program'
        return True

    def emptyline(self):
        """overwriting the emptyline method"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
