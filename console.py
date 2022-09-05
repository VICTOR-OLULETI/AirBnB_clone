#!/usr/bin/python3
"""This program is responsible for the console/interactive part of the hbnb"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

classes = {
            'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity,
            'Place': Place, 'Review': Review
          }

methods = ['all', 'count', 'show', 'destroy', 'update']


class HBNBCommand(cmd.Cmd):
    """Class definition for basic HBNB commands"""
    """ intro = 'Welcome to the HBNB console.
    Type help or ? to listcommands.\n'
    """
    prompt = '(hbnb) '
    if not sys.__stdin__.isatty():
        prompt = ''
    # all_objs = storage.all()
    # ----- basic HBNB commands -----

    def precmd(self, line):
        """Usage: <class name>.all()"""
        if not ('.' in line and '(' in line and ')' in line):
            return line
        arg = ''
        opt = ''
        temp = line[:]
        cls = temp[:temp.find('.')]
        mth = temp[temp.find('.') + 1: temp.find('(')]
        arg = temp[temp.find('(') + 1: temp.find(')')]
        arg = arg.replace('"', '', 2)
        if mth not in methods:
            raise Exception

        command = ' '.join([mth, cls, arg])

        return command

    def preloop(self):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    '''
    def postcmd(self, stop, line):
        """Prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('hbnb ', end='')
            return stop
    '''
    def postloop(self):
        """prints if isatty is false"""
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def do_create(self, arg):
        """Creates the object instance"""
        args = arg.split()
        if args is None or len(args) == 0:
            print('** class name missing **')
            return False
        if (args[0] in classes):
            Instance = classes[args[0]]()
            Instance.save()
        else:
            print("** class doesn't exist **")
            return False
        print(Instance.id)

    def do_show(self, arg):
        """Displays the object instance"""
        args = arg.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
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

    def do_count(self, arg):
        """Prints the number of instance of an object"""
        count = 0
        all_objs = storage.all()
        args = arg.split()
        for obj_id in all_objs.keys():
            if (obj_id.split('.')[0] == args[0]):
                count += 1
        print(count)

    def do_update(self, arg):
        "updates the obj instance"
        args = arg.split()
        temp = arg.split(',')
        all_objs = storage.all()
        if args is None or len(args) == 0:
            print("** class name missing **")
            return False
        if (args[0] not in classes):
            print("** class doesn't exist **")
            return False
        if (len(args) == 1):
            print("** instance id missing **")
            return False
        all_objs = storage.all()
        args[1] = args[1].split(',')[0]
        key = args[0] + '.' + args[1]
        if key not in all_objs:
            print("** no instance found **")
            return False
        if (len(args) == 2):
            print("** attribute name missing **")
            return False
        if (len(args) == 3):
            print("** value missing **")
            return False
        if (len(args) >= 4):
            all_obj_key = all_objs[key]
            print(temp)
            print(args)
            if (len(temp) == 3):
                temp1 = temp[1]
                temp2 = temp[2]
                temp3 = ', '.join([temp1, temp2])
                if '{' in temp[1] and type(eval(temp3)) is dict:
                    dict_arg = eval(temp3)
                    for key, value in dict_arg.items():
                        if (type(value) is str):
                            value = value.replace('"', '', 2)
                        setattr(all_obj_key, key, value)
            else:
                # all_obj_key[args[2]] = args[3]
                args[3] = args[3].replace('"', '', 2)
                setattr(all_obj_key, args[2], args[3])
            all_obj_key.save()

    def do_destroy(self, arg):
        """ destroys an instance of the obj """
        args = arg.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
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
            Instance = classes[args[0]]()
            del all_objs[key]
            # Instance.save()
            storage.save()

    def do_all(self, arg):
        """Displays all the object instances"""
        result = []
        args = arg.split()
        all_objs = storage.all()
        if (len(args) >= 1):
            if (args[0] not in classes):
                print("** class doesn't exist **")
                return False
        if (len(args) == 1):
            for obj_id in all_objs.keys():
                if (obj_id.split('.')[0] == args[0]):
                    obj = all_objs[obj_id]
                    result.append(str(obj))

        elif (len(args) == 0):
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
