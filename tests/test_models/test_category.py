#!/usr/bin/python3
"""Defining the test case for category class"""

from models.category import (Category, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
Category = models.category.Category
category_doc = models.category.__doc__


class TestCategoryDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.category_f = inspect.getmembers(Category, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that categoryl conforms with pep8"""
        for path in ['models/category.py',
                     'tests/test_models/test_category.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(category_doc, None,
                         'category.py needs a docstring')
        self.assertTrue(len(category_doc) > 1,
                        'category.py needs a docstring')

    def test_class_docstring(self):
        """Test for Category class docstring"""
        self.assertIsNot(Category.__doc__, None,
                         'Category needs a docstring')
        self.assertTrue(len(Category.__doc__) >= 1,
                        'Category needs a docstring')


class TestCategory(unittest.TestCase):
    """test representation for User"""

    def test_category_type(self):
        """testing for first name attribute for user model"""
        category = Category()
        self.assertTrue(category, "category_type")
        self.assertEqual(category.category_type, "")
        self.assertEqual(type(Category.category_type), str)

    def test_attribute(self):
        """Testing for the attribute of all the user class"""
        category = Category()
        self.assertTrue(hasattr(category, "category_type"))
        self.assertTrue(hasattr(category, "id"))
        self.assertTrue(hasattr(category, "created_at"))
        self.assertTrue(hasattr(category, "updated_at"))

    def test_input(self):
        """testing the various input for category"""
        category = Category()
        category.category_type = "Male"
        self.assertEqual(category.category_type, "Male")
