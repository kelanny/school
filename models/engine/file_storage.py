#!usr/bin/env python3
"""Serializes instances to a JSON file and deserializes JSON file to instances"""

import json
import os.path
from os import path
import importlib
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists; otherwise, do nothing)"""
        if path.exists(self.__file_path):
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    for i, letter in enumerate(class_name[1:], 1):
                        if letter.isupper():
                            module_name = f"models.{class_name[:i].lower()}_{class_name[i:].lower()}"
                    try:
                        cls = getattr(importlib.import_module(module_name), class_name)
                        self.__objects[key] = cls(**value)
                    except Exception as e:
                        print(f"Error loading object {key}: {e}")