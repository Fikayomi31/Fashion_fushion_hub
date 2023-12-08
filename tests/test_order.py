#!/usr/bin/python3
"""Defining the test case for order class"""

from models.order import (Order, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
Order = models.order.Order
order_doc = models.order.__doc__


class TestOrderDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.order_f = inspect.getmembers(Order, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that order conforms with pep8"""
        for path in ['models/order.py',
                     'tests/test_order.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(order_doc, None,
                         'order.py needs a docstring')
        self.assertTrue(len(order_doc) > 1,
                        'order.py needs a docstring')

    def test_class_docstring(self):
        """Test for Order class docstring"""
        self.assertIsNot(Order.__doc__, None,
                         'Order needs a docstring')
        self.assertTrue(len(Order.__doc__) >= 1,
                        'Order needs a docstring')


class TestOrder(unittest.TestCase):
    """test representation for Order"""

    def test_user_id(self):
        """testing for user_id attribute for order model"""
        order = Order()
        self.assertTrue(order, "user_id")
        self.assertEqual(order.user_id, "")
        self.assertEqual(type(order.user_id), str)

    def test_order_date(self):
        """Testing for order_date attribute for order model"""
        order = Order()
        self.assertTrue(order, "order_date")
        self.assertEqual(order.order_date, "")
        self.assertEqual(type(order.order_date), str)

    def test_total_amount(self):
        """Testing for total_amount attributes for order model"""
        order = Order()
        self.assertTrue(order, "order_amount")
        self.assertEqual(order.total_amount, 0.0)
        self.assertEqual(type(order.total_amount), float)

    def test_attribute(self):
        """Testing for the attribute of all the user class"""
        order = Order()
        self.assertTrue(hasattr(order, "user_id"))
        self.assertTrue(hasattr(order, "order_date"))
        self.assertTrue(hasattr(order, "total_amount"))
        self.assertTrue(hasattr(order, "id"))
        self.assertTrue(hasattr(order, "created_at"))
        self.assertTrue(hasattr(order, "updated_at"))

    def test_input(self):
        """testing the various input for order"""
        order = Order()
        order.user_id = "34"
        order.order_date = "20-12-2018"
        order.total_amount = 2000.00

        self.assertEqual(order.user_id, "34")
        self.assertEqual(order.order_date, "20-12-2018")
        self.assertEqual(order.total_amount, 2000.00)
