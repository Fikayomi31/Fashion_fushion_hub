#!/usr/bin/python3
"""Defining the class product type"""
from models.base_model import BaseModel
from sqlalchemy import Integer, Column, String, ForeignKey
from os import getenv

storage_type = getenv('FFH_TYPE_STORAGE')


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
    if storage_type == 'db':
        product_name = Column(String(1024), nullable=False)
        brand_id = Column(String(60), ForeignKey('brand.id'), nullable=False)
        category_id = Column(String(60), ForeignKey('category.id'), nullable=False)
        price = Column(Integer)
        stock_quantity = Column(Integer)
        text = Column(String(1024))
    else:
        product_name = ""
        brand_id = ""
        category_id = ""
        price = ""
        stock_quantity = ""
        text = ""
