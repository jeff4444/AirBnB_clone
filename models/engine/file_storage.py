#!/usr/bin/python3
"""File storage module"""


import json
import models


class FileStorage:
    __file_path = 'storage.json'
    __objects = {}

    def all(self):
        """Returns all objecrs"""

        return self.__objects

    def new(self, obj):
        """Adds a new object to our objects dict"""

        self.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """Save our object dict to our file path"""

        dict_to_save = {}
        for key, val in self.__objects.items():
            dict_to_save[key] = val.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(dict_to_save, f)

    def reload(self):
        """Reloads objects from file path"""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                dict_loaded = json.load(f)
                class_dicts = {'BaseModel': models.base_model.BaseModel,
                               'User': models.user.User,
                               'Place': models.place.Place,
                               'Review': models.review.Review,
                               'City': models.city.City,
                               'Amenity': models.amenity.Amenity,
                               'State': models.state.State,
                               }
                for key1, val in dict_loaded.items():
                    for key in class_dicts:
                        if key1[0:len(key)] == key:
                            self.__objects[key1] = class_dicts[key](**val)
        except FileNotFoundError:
            return
