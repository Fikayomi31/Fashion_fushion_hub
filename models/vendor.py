#!/usr/bin/python3
"""Defining the class for  vendor"""
from models.base_model import BaseModel


class Vendor(BaseModel):
    """Vendor class representation"""
    vendor_shop_name: str = ""
    vendor_address: str = ""
    email: str = ""
    phone: str = ""
    password: str = ""

