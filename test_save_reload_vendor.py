#!/usr/bin/python3
from models.base_model import BaseModel
from models import storage
from models.vendor import Vendor

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new Vendor --")
my_vendor = Vendor()
my_vendor.vendor_name = "Nola"
my_vendor.email = "nolaband@gmail.com"
my_vendor.password = "root"
my_vendor.phone = "+23470367345623"
my_vendor.address = "23 Maja street  Yaba"
my_vendor.save()
print(my_vendor)

print("-- Create a new Vendor --")
my_vendor2 = Vendor()
my_vendor.shop_name = "Habit"
my_vendor.email = "habitband@gmail.com"
my_vendor.password = "root"
my_vendor.phone = "+2348067345623"
my_vendor.address = "45 Oli street Lekki VI"
my_vendor2.save()
print(my_vendor2)
