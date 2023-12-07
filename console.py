#!/usr/bin/python3
"""cmd implemented"""
import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.vendor import Vendor
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from models.review import Review

classnames = {
        "BaseModel": BaseModel,
        "User": User,
        "Vendor": Vendor,
        "Product": Product,
        "Order": Order,
        "OrderItem": OrderItem,
        "Review": Review
        }

def parse_arg(arg):
    """parse and separates args"""
    return arg.split(" ")

def rem_chars(my_list):
    """remove the \" or \' character"""
    for i in range(len(my_list)):
        if my_list[i][0] == '"' or my_list[i][0] == "'":
            my_list[i] = my_list[i][1: -1]
        return my_list

class FFHCommand(cmd.Cmd):
    """Entry loint to the command"""
    prompt = '(ffh) '

    def do_EOF(self, arg):
        """ctrl+D to exit the program"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Empty line + enter doesnot execute anything"""
        return False

    def do_create(self, arg):
        """creates the instance of the variable"""
        if arg:
            if arg not in classnames:
                print("** class name doesn't exist **")
            else:
                print(eval(arg)().id)
                storage.save()
        else:
            print("** class name missing **")
    
    def do_show(self, arg):
        """show the object based on id"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            else:
                print(all_objs[f"{arg_list[0]}.{arg_list[1]}"])
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """destroy an object from the database"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:                                                                              print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            else:
                del all_objs[f"{arg_list[0]}.{arg_list[1]}"]
                storage.save()
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """list all the BaseModel store"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        result = []
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            else:
                for key, value in all_objs.items():
                    classname, id = key.split(".")
                    if arg_list[0] == classname:
                        result.append(all_objs[key].__str__())
                print(result)
        else:
            for obj_id in all_objs.keys():
                result.append(all_objs[key].__str__())
            print(result)

    def do_update(self, arg):
        """update an attribute in an object"""
        arg_list = parse_arg(arg)
        all_objs = storage.all()
        if arg_list[0]:
            if arg_list[0] not in classnames:
                print("** class doesn't exist **")
            elif len(arg_list) == 1:
                print("** instance id missing **")
            elif f"{arg_list[0]}.{arg_list[1]}" not in all_objs:
                print("** no instance found **")
            elif len(arg_list) == 2:
                print("** attribute name missing **")
            elif len(arg_list) == 3:
                print("** value missing **")
            else:
                obj = all_objs[f"{arg_list[0]}.{arg_list[1]}"]
                for i in range(2, len(arg_list), 2):
                    if arg_list[i + 1][0] == '"' and arg_list[i + 1][-1] == '"':
                        arg_list[i + 1] = arg_list[i + 1][1: -1]
                    if arg_list[i] in obj.to_dict():
                        val_type = type(getattr(obj, arg_list[i]))
                        setattr(obj, arg_list[i], val_type(arg_list[i + 1]))
                    else:
                        setattr(obj, arg_list[i], arg_list[i + 1])
                storage.save()
        else:
            print("** class name missing **")



if __name__ == "__main__":
    FFHCommand().cmdloop()
