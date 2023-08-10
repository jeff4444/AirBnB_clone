#!/usr/bin/python3
"""File storage module"""


import json
import models


class FileStorage:
    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        dict_to_save = {}
        for key, val in self.__objects.items():
            dict_to_save[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_to_save, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dict_loaded = json.load(f)
                for key, val in dict_loaded.items():
                    self.__objects[key] = models.base_model.BaseModel(**val)
        except FileNotFoundError:
            return
