#!/usr/bin/python3

"""
Contains FileStorage class
"""


import json
import os


class FileStorage:
    """
    Serializes instances JSON file and deesrializes JSON file to an instance
    """

    __file_path = './file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        # serializes __objects to json file
        new = {}
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            for k, v in self.__objects.items():
                # print("saved obj")
                # print("v = ", v, "k= ", k, "\n")
                key = "{}.{}".format(v['__class__'], v['id'])
                new[key] = v
            json.dump(new, f)

    def reload(self):
        # desrializes json file into __objects
        exists = os.path.isfile(self.__file_path)
        if (exists):
            with open(self.__file_path, encoding='utf-8') as f:
                newDict = json.load(f)
                c = '__class__'
                for k, v in newDict.items():
                    # print("reloaded obj")
                    self.__objects[k] = v
