#!/usr/bin/python3
"""This module create the class FileStorage"""

import json


class FileStorage():
    '''serializes instances to a JSON file and deserializes
       JSON file to instances
    '''
    __file_path = file.json
    __objects = {}

    def all(self):
        '''returns the dict `__objects`'''
        return self.__objects

    def new(self, obj):
        '''sets in `__objects` the `obj` with key `<obj class name>.id`'''
        name = obj.__class__.__name__
        _id = obj.__dict__.id
        key = f'{name}.{id}'
        self.__objects[key] = obj

    def save(self):
        '''serializes `__objects` to the JSON file'''
        with (self.__file_path, 'w') as file:
            json.dump(self.__objects, file)

    def reload(self):
        '''deserializes the JSON file to `__objects`'''
        try:
            with (self.__file_path) as file:
                new_obj = json.loads(file)
                
            

