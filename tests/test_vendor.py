#!/usr/bin/python3
"""Defining the test case for user class"""

from models.vendor import (Vendor, BaseModel)
import unittest


class TestUser(unittest.TestCase):
    """test representation for User"""

    def setUp(self):
        """setting up test cases for user"""
        self.vendor = Vendor()

    def tearDown(self):
        """Deleting the test cases"""
        del self.vendor

    def test_classattr(self):
        """testing the public class attribute for vendor model"""
        vendor = self.vendor
        self.assertEqual(vendor.email, "")
        self.assertEqual(vendor.password, "")
        self.assertEqual(vendor.vendor_name, "")
        self.assertEqual(vendor.phone, "")
        self.assertEqual(vendor.address, "")
    
    def test_input(self):
        """testing the various input for vendor"""
        vendor = self.vendor
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
