#!/usr/bin/python3
"""Defining the class for FFH console"""
import cmd
from datetime import datetime
import models
from models.base_model import BaseModel
from models.user import User
from models.brand import Vendor
from models.category import Category
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from models.review import Review
import shlex

classes = {
        "BaseModel": BaseModel,
        "User": User,
        "Vendor": Vendor,
        "Category": Category,
        "Product": Product,
        "Order": Order,
        "OrderItem": OrderItem,
        "Review": Review
        }


class FFHCommand(cmd.Cmd):
    """FFH console"""
    prompt = '(ffh) '

    def do_EOF(self, arg):
        """Exit the console"""
        return True

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_emptyline(self, arg):
        """emptyline method"""
        return False

    def _key_value_parser(self, args):
        """create a dict from list od string"""
        new_dict = {}
        for arg in args:
            if "=" in arg:
                kvp = arg.split("=", 1)
                key = arg[0]
                value = arg[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except Exception:
                        try:
                            value = float(value)
                        except Exception:
                            continue
                new_dict[key] = value
        return new_dict

    def do_create(self, arg):
        """create a new BaseModel instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            new_dict = self._key_value_parser(args[1:])
            instance = classes[args[0]](**new_dict)
        else:
            print("** class doesn't exist **")
            return False
        print(instance.id)
        instance.save()

    def do_show(self, arg):
        """print an instance as a sting base on id and class"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return False
        if args[0] in classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destory(self, arg):
        """Delete an instance base on class and id"""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                key = args[0] + '.' + arg[1]
                if key in models.storage.all(classes[args[0]]):
                    models.storage.all().pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """print string representation of instance"""
        args = shlex.split(arg)
        obj_list = []
        if len(args) == 0:
            obj_dict = models.storage.all()
        elif args[0] in classes:
            obj_dict = models.storage.all(classes[args[0]])
        else:
            print("** class doesn't exist **")
            return False
        for key in obj_dict:
            obj_list.append(str(obj_dict[key]))
        print("[", end="")
        print(", ".join(obj_list), end="")
        print("]")

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        args = shlex.split(arg)
        integers = ["number_rooms", "number_bathrooms", "max_guest",
                    "price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in models.storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except Exception:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except Exception:
                                        args[3] = 0.0
                            setattr(models.storage.all()[k], args[2], args[3])
                            models.storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """count the number of instance"""
        objs = models.storage.all()
        if arg in classes:
            obj_list = [obj.to_dict for obj in objs.values()
                        if obj.to_dict().get("__class__") == arg]
            print(len(obj_list))

    def default(self, arg):
        """Default command overwrite
        """
        args = arg.split(".")
        class_name = args[0]
        commands = {
                "all": self.do_all,
                "count": self.do_count,
                "show": self.do_show,
                "destory": self.do_destory,
                "update": self.do_update,
                "create": self.do_create
                }
        command_arg = args[1].replace('(', ' ')\
                             .replace(',', '').replace(')', ' ')\
                             .split()
        command = command_arg[0]
        if command in commands:
            if command in ["all", "count", "create"]:
                commands[command](class_name)
            elif command in ["show", "destory"]:
                commands[command](class_name + " " + command_arg[1])
            elif command in ["update"]:
                commands[command](class_name + " " + command_arg[1]
                                  + " " + command_arg[2] + " "
                                  + command_arg[3])


if __name__ == "__main__":
    FFHCommand().cmdloop()
