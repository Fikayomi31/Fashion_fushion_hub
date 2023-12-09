#!/usr/bin/python3
"""Defining the test case for order_item class"""

from models.order_item import (OrderItem, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
OrderItem = models.order_item.OrderItem
order_item_doc = models.order_item.__doc__


class TestOrderItemDocs(unittest.TestCase):
    """Test to check for documentation and style of OrderItem class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.order_item_f = inspect.getmembers(OrderItem, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that order_item conforms with pep8"""
        for path in ['models/order_item.py',
                     'tests/test_models/test_order_item.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(order_item_doc, None,
                         'order_item.py needs a docstring')
        self.assertTrue(len(order_item_doc) > 1,
                        'order_item.py needs a docstring')

    def test_class_docstring(self):
        """Test for OrderItem class docstring"""
        self.assertIsNot(OrderItem.__doc__, None,
                         'OrderItem needs a docstring')
        self.assertTrue(len(OrderItem.__doc__) >= 1,
                        'OrderItem needs a docstring')


class TestOrderItem(unittest.TestCase):
    """test representation for OrderItem"""

    def test_user_id(self):
        """testing for user_id attribute for order item model"""
        order_item = OrderItem()
        self.assertTrue(order_item, "user_id")
        self.assertEqual(order_item.user_id, "")
        self.assertEqual(type(order_item.user_id), str)

    def test_order_id(self):
        """testing for order_id attribute for order item model"""
        order_item = OrderItem()
        self.assertTrue(order_item, "order_id")
        self.assertEqual(order_item.order_id, "")
        self.assertEqual(type(order_item.order_id), str)

    def test_product_id(self):
        """Testing for product_id attribute for order item model"""
        order_item = OrderItem()
        self.assertTrue(order_item, "product_id")
        self.assertEqual(order_item.product_id, [])
        self.assertEqual(type(order_item.product_id), list)

    def test_subtotal(self):
        """Testing for total_amount attributes for order model"""
        order_item = OrderItem()
        self.assertTrue(order_item, "subtotal")
        self.assertEqual(order_item.subtotal, 0.0)
        self.assertEqual(type(order_item.subtotal), float)

    def test_quantity(self):
        """Testing for quantity attributes for order item model"""
        order_item = OrderItem()
        self.assertTrue(order_item, "quantity")
        self.assertEqual(order_item.quantity, 0)
        self.assertEqual(type(order_item.quantity), int)

    def test_attribute(self):
        """Testing for the attribute of all the order item class"""
        order_item = OrderItem()
        self.assertTrue(hasattr(order_item, "user_id"))
        self.assertTrue(hasattr(order_item, "order_id"))
        self.assertTrue(hasattr(order_item, "product_id"))
        self.assertTrue(hasattr(order_item, "subtotal"))
        self.assertTrue(hasattr(order_item, "quantity"))
        self.assertTrue(hasattr(order_item, "id"))
        self.assertTrue(hasattr(order_item, "created_at"))
        self.assertTrue(hasattr(order_item, "updated_at"))

    def test_input(self):
        """testing the various input for order item"""
        order_item = OrderItem()
        order_item.user_id = "34"
        order_item.order_id = "20"
        order_item.product_id = [1, 2]
        order_item.subtotal = 2000.00
        order_item.quantity = 12
        self.assertEqual(order_item.user_id, "34")
        self.assertEqual(order_item.order_id, "20")
        self.assertEqual(order_item.product_id, [1, 2])
        self.assertEqual(order_item.subtotal, 2000.00)
        self.assertEqual(order_item.quantity, 12)
