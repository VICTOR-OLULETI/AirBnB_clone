#!/usr/bin/python3
"""
This program is the File Storage
"""
import json
import os

class FileStorage:
    """This is the file Storage class"""
    # private class attributes
    __file_path='file.json'
    __objects = {}

    # Public instance Methods
    def all(self):
        """Returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = str(type(obj).__name__)+('.') + obj.id
        dict_all = self.all()
        dict_all[key] = (obj)

    def save(self):
        """serializes __objects to the JSON file(path:__file_path)"""
         
        filename = FileStorage.__file_path
        temp = {}
        with open(filename, mode="w", encoding="utf-8") as myFile:
            """
            temp.update(FileStorage.__objects)
            
            for key, val in temp.items():
                temp[key] = val.to_dict()
            
            """
            for key in FileStorage.__objects:
                temp[key] = FileStorage.__objects[key].to_dict()
        
            json.dump(temp, myFile, sort_keys=True, indent=4)
        
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
        classes = { 'BaseModel': BaseModel}
        filename = FileStorage.__file_path
        try:
            if os.path.exists(filename):
                with open(filename, mode="r") as myFile:
                    content_out = json.load(myFile)
                    for key, val in content_out.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except:
            pass
