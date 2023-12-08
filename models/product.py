#!/usr/bin/python3
"""Defining the class product type"""
from models.base_model import BaseModel


class Product(BaseModel):
    """product class representation
    Attributes:
        vendor_id(str) - the vendor id
        catetory_id(str) - the cateory id
        product_name(str) - the product name
        price (float) - the product price
        stock_quantity (int) - the product quantity
        text(str) - the text for the product
    """
    vendor_id = ""
    category_id = ""
    product_name = ""
    price = 0.0
    stock_quantity = 0
    text = ""
