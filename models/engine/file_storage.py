#!/usr/bin/python3
"""file storage class"""

import json


class FileStorage:
    """the class for serialization and deserialization of clas
    Attributes:
        __file_path (str) - path to the json file
        __object (dict) - dict to store all the object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the dictionary __object"""
        return self.__objects

    def new(self, obj):
        """set in __object the obj with key id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the json file path"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def classes(self):
        """Returning the valid class of dict"""
        from models.base_model import BaseModel
        from models.user import User
        from models.vendor import Vendor
        from models.product import Product
        from models.order import Order
        from models.order_item import OrderItem
        from models.reveiw import Review
        classes = {
                "BaseModel": BaseModel,
                "User": User,
                "Vendor": Vendor,
                "Product": Product,
                "Order": Order,
                "OderItem": OrderItem,
                "Review": Review
                }

        return classes

    def reload(self):
        """deserializes the json file to __objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {k: self.classes()[v["__class__"]](**v)
                            for k, v in obj_dict.items()}
                self.__objects = obj_dict
        except Exception:
            pass
