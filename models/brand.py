#!/usr/bin/python3
"""Defining the class for  vendor"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, ForeignKey

storage_type = getenv('FFH_TYPE_STORAGE')


class Brand(BaseModel, Base):
    """Vendor class representation"""
    __table__ = 'brands'
    if storage_type == 'db':
        brand_name = Column(String(60), nullable=False)
        # brand_id = Column
    else:
        brand_name = ""
    
