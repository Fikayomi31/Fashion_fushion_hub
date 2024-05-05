#!/usr/bin/python3
""" Test delete feature
"""
from models.engine.file_storage import FileStorage
from models.brand import Brand

fs = FileStorage()

# all Brands
all_brands = fs.all(Brand)
print("All Brands: {}".format(len(all_brands.keys())))
for brand_key in all_brands.keys():
    print(all_brands[brand_key])

# Create a new brand
new_brand = Brand()
new_brand.name = 'Habit'
fs.new(new_brand)
fs.save()
print("New Brand: {}".format(new_brand))

# All Brands
all_brands = fs.all(Brand)
print("All Brands: {}".format(len(all_brands.keys())))
for brand_key in all_brands.keys():
    print(all_brands[brand_key])

# Delete the new Brand
fs.delete(new_brand)

# All Brands
all_brands = fs.all(Brand)
print("All Brands: {}".format(len(all_brands.keys())))
for brand_key in all_brands.keys():
    print(all_brands[brand_key])
    