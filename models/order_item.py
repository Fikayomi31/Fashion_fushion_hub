#!/usr/bin/python3
"""Defining the class of Order items"""
from models.base_model import BaseModel


class OrderItem(BaseModel):
    """Representation of each order item
    Attribute:
        user_id (str) - the user id
        order_id (str) - the order id
        quantity (int) - the quantity purchase
        product_id []- the product id
        subtotal (float) - the subtotal of the item
    """
    user_id = ""
    order_id = ""
    quantity = 0
    product_id = []
    subtotal = 0.0
