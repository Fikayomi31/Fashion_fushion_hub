#!/usr/bin/python3
"""Defining the class product type"""
from models.base_model import BaseModel


class Product(BaseModel):
    """product class representation
    Attributes:
        vendor_id(str) - the vendor id
        catetory_id(str) - the cateory id
        name(str) - the product name
        color(str) - the product color
        price(str) - the product price
        stock_quantity(str) - the product quantity
        text(str) - the text for the product
    """
    vendor_id = ""
    category_id = ""
    name = ""
    color = ""
    pricr = ""
    stock_quantity = ""
    text = ""
