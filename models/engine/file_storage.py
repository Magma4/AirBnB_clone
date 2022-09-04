#!/usr/bin/python3
"""the file storage class:
This class stores an istance into a file in JSON
readable and writable by all programming languages
"""

import json
import os


class FileStorage:
    """the file storage class define funcs to save to a file
    in json and load to a python object.
    the all method returns all the objects and the new method adds
    a new object
    """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        """returns the dictionary __objects
        as stored in the __objects variable upon creation
        """
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the object with key
        objclassname.id
        """
        obj_key = "{:s}.{:s}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the json
        file path __file_path
        """
        obj_clone = dict.copy(FileStorage.__objects)
        for key, value in obj_clone.items():
            obj_clone[key] = value.to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(obj_clone))

    def reload(self):
        """deserializes the json file to
        __objects if the json file exist
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                obj_clone = json.loads(f.read())
                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.city import City
                from models.state import State
                from models.review import Review
                from models.amenity import Amenity
                for key, value in obj_clone.items():
                    if (obj_clone[key])['__class__'] == "BaseModel":
                        obj_clone[key] = BaseModel(**value)
                    elif (obj_clone[key])['__class__'] == "User":
                        obj_clone[key] = User(**value)
                    elif (obj_clone[key])['__class__'] == "Place":
                        obj_clone[key] = Place(**value)
                    elif (obj_clone[key])['__class__'] == "City":
                        obj_clone[key] = City(**value)
                    elif (obj_clone[key])['__class__'] == "State":
                        obj_clone[key] = State(**value)
                    elif (obj_clone[key])['__class__'] == "Review":
                        obj_clone[key] = Review(**value)
                    elif (obj_clone[key])['__class__'] == "Amenity":
                        obj_clone[key] = Amenity(**value)
                FileStorage.__objects = dict.copy(obj_clone)
