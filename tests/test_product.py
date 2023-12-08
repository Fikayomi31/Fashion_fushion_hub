#!/usr/bin/python3
"""Defining the test case for product class"""

from models.product import (Product, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
Product = models.product.Product
product_doc = models.product.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Test to check for documentation and style of Product class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.product_f = inspect.getmembers(Product, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that product conforms with pep8"""
        for path in ['models/product.py',
                     'tests/test_product.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(product_doc, None,
                         'product.py needs a docstring')
        self.assertTrue(len(product_doc) > 1,
                        'product.py needs a docstring')

    def test_class_docstring(self):
        """Test for Product class docstring"""
        self.assertIsNot(Product.__doc__, None,
                         'Product needs a docstring')
        self.assertTrue(len(Product.__doc__) >= 1,
                        'Product needs a docstring')


class TestProduct(unittest.TestCase):
    """test representation for User"""

    def test_product_id(self):
        """testing for vendor_id attribute for Product model"""
        product = Product()
        self.assertTrue(product, "vendor_id")
        self.assertEqual(product.vendor_id, "")
        self.assertEqual(type(product.vendor_id), str)

    def test_category_id(self):
        """Testing for category_id attribute for product model"""
        product = Product()
        self.assertTrue(product, "category_id")
        self.assertEqual(product.category_id, "")
        self.assertEqual(type(product.category_id), str)

    def test_product_name(self):
        """Testing for product name attributes for product model"""
        product = Product()
        self.assertTrue(product, "product_name")
        self.assertEqual(product.product_name, "")
        self.assertEqual(type(product.product_name), str)

    def test_price(self):
        """Testing for price attributes for product model"""
        product = Product()
        self.assertTrue(product, "price")
        self.assertEqual(product.price, 0.0)
        self.assertEqual(type(product.price), float)

    def test_stock_quantity(self):
        """Testing for quantity attributes for product model"""
        product = Product()
        self.assertTrue(product, "stock_quantity")
        self.assertEqual(product.stock_quantity, 0)
        self.assertEqual(type(product.stock_quantity), int)

    def test_text(self):
        """Testing for text attributes for product model"""
        product = Product()
        self.assertTrue(product, "text")
        self.assertEqual(product.text, "")
        self.assertEqual(type(product.text), str)

    def test_attribute(self):
        """Testing for the attribute of all the product class"""
        product = Product()
        self.assertTrue(hasattr(product, "vendor_id"))
        self.assertTrue(hasattr(product, "category_id"))
        self.assertTrue(hasattr(product, "product_name"))
        self.assertTrue(hasattr(product, "price"))
        self.assertTrue(hasattr(product, "stock_quantity"))
        self.assertTrue(hasattr(product, "text"))
        self.assertTrue(hasattr(product, "id"))
        self.assertTrue(hasattr(product, "created_at"))
        self.assertTrue(hasattr(product, "updated_at"))

    def test_input(self):
        """testing the various input for vendor"""
        product = Product()
        product.vendor_id = "34"
        product.category_id = "23"
        product.product_name = "Habit"
        product.price = 2345.01
        product.stock_quantity = 23
        product.text = "Vercity"

        self.assertEqual(product.vendor_id, "34")
        self.assertEqual(product.category_id, "23")
        self.assertEqual(product.product_name, "Habit")
        self.assertEqual(product.price, 2345.01)
        self.assertEqual(product.stock_quantity, 23)
        self.assertEqual(product.text, "Vercity")
