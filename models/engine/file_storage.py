#!/usr/bin/python3
"""
This program is the File Storage
"""
import json
import os
"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
"""


class FileStorage:
    """This is the file Storage class"""
    # private class attributes
    __file_path = 'file.json'
    __objects = {}

    # Public instance Methods
    def all(self):
        """Returns the dictionary"""
        return (self.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(type(obj).__name__)+('.') + obj.id
        dict_all = self.all()
        dict_all[key] = (obj)

    def save(self):
        """serializes __objects to the JSON file(path:__file_path)"""
        filename = FileStorage.__file_path
        temp = {}
        with open(filename, mode="w") as myFile:
            """
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            """
            """
            for key in FileStorage.__objects:
                temp[key] = FileStorage.__objects[key].to_dict()
            """
            for key, value in FileStorage.__objects.items():
                temp[key] = value.to_dict()
            json.dump(temp, myFile, sort_keys=True, indent=4)
            #json.dump(temp, myFile, sort_keys=True)
        """
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f, sort_keys=True, indent=4)
        """
    def reload(self):
        """deserializes the JSON file to __objects
        only if the JSON file exitst
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User,
                    'State': State, 'City': City,
                    'Amenity': Amenity, 'Place': Place,
                    'Review': Review
                  }
        filename = FileStorage.__file_path
        try:
            if os.path.exists(filename):
                content_out = {}
                with open(filename, mode="r") as myFile:
                    content_out = json.load(myFile)
                    for key, val in content_out.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
        # ValueError
