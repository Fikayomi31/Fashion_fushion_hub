#!/usr/bin/python3
"""Defining the test case for user class"""

from models.vendor import (Vendor, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
Vendor = models.vendor.Vendor
vendor_doc = models.vendor.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.vendor_f = inspect.getmembers(Vendor, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that base_model conforms with pep8"""
        for path in ['models/vendor.py',
                     'tests/test_vendor.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(vendor_doc, None,
                         'vendor.py needs a docstring')
        self.assertTrue(len(vendor_doc) > 1,
                        'vendor.py needs a docstring')

    def test_class_docstring(self):
        """Test for BaseModel class docstring"""
        self.assertIsNot(Vendor.__doc__, None,
                         'Vendor needs a docstring')
        self.assertTrue(len(Vendor.__doc__) >= 1,
                        'Vendor needs a docstring')


class TestVendor(unittest.TestCase):
    """test representation for User"""

    def test_vendor_name(self):
        """Testing for vendor_name for vendor name"""
        vendor = Vendor()
        self.assertTrue(vendor, "vendor_name")
        self.assertEqual(vendor.vendor_name, "")
        self.assertEqual(type(vendor.vendor_name), str)

    def test_password(self):
        """Testing for password for vendor class"""
        vendor = Vendor()
        self.assertTrue(vendor, "password")
        self.assertEqual(vendor.password, "")
        self.assertEqual(type(vendor.password), str)

    def test_email(self):
        """Testing for email for vendor class"""
        vendor = Vendor()
        self.assertTrue(vendor, "email")
        self.assertEqual(vendor.email, "")
        self.assertEqual(type(vendor.email), str)

    def test_phone(self):
        """Testing for phone number for vendor class"""
        vendor = Vendor()
        self.assertTrue(vendor, "phone")
        self.assertEqual(vendor.phone, "")
        self.assertEqual(type(vendor.phone), str)

    def test_address(self):
        """Testing for address for vendor class"""
        vendor = Vendor()
        self.assertTrue(vendor, "address")
        self.assertEqual(vendor.address, "")
        self.assertEqual(type(vendor.address), str)

    def test_attribute(self):
        """Test for the attributes of vendor class"""
        vendor = Vendor()
        self.assertTrue(hasattr(vendor, "vendor_name"))
        self.assertTrue(hasattr(vendor, "email"))
        self.assertTrue(hasattr(vendor, "password"))
        self.assertTrue(hasattr(vendor, "phone"))
        self.assertTrue(hasattr(vendor, "address"))
        self.assertTrue(hasattr(vendor, "id"))
        self.assertTrue(hasattr(vendor, "created_at"))
        self.assertTrue(hasattr(vendor, "updated_at"))

    def test_input(self):
        """testing the various input for vendor"""
        vendor = Vendor()
        vendor.email = "peterjohn@mail.com"
        vendor.password = "root"
        vendor.vendor_name = "peter"
        vendor.phone = "030138372"
        vendor.address = "45 wole strret Wale England"

        self.assertEqual(vendor.email, "peterjohn@mail.com")
        self.assertEqual(vendor.password, "root")
        self.assertEqual(vendor.vendor_name, "peter")
        self.assertEqual(vendor.phone, "030138372")
        self.assertEqual(vendor.address, "45 wole strret Wale England")
