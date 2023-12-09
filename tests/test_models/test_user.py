#!/usr/bin/python3
"""Defining the test case for user class"""

from models.user import (User, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
User = models.user.User
user_doc = models.user.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that base_model conforms with pep8"""
        for path in ['models/user.py',
                     'tests/test_models/test_user.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(user_doc, None,
                         'user.py needs a docstring')
        self.assertTrue(len(user_doc) > 1,
                        'user.py needs a docstring')

    def test_class_docstring(self):
        """Test for BaseModel class docstring"""
        self.assertIsNot(User.__doc__, None,
                         'User needs a docstring')
        self.assertTrue(len(User.__doc__) >= 1,
                        'User needs a docstring')


class TestUser(unittest.TestCase):
    """test representation for User"""

    def test_first_name(self):
        """testing for first name attribute for user model"""
        user = User()
        self.assertTrue(user, "first_name")
        self.assertEqual(user.first_name, "")
        self.assertEqual(type(user.first_name), str)

    def test_last_name(self):
        """Testing for last name attribute for user model"""
        user = User()
        self.assertTrue(user, "last_name")
        self.assertEqual(user.last_name, "")
        self.assertEqual(type(user.last_name), str)

    def test_password(self):
        """Testing for password attributes for user model"""
        user = User()
        self.assertTrue(user, "last_name")
        self.assertEqual(user.password, "")
        self.assertEqual(type(user.password), str)

    def test_email(self):
        """Testing for email attributes for user model"""
        user = User()
        self.assertTrue(user, "last_name")
        self.assertEqual(user.email, "")
        self.assertEqual(type(user.email), str)

    def test_attribute(self):
        """Testing for the attribute of all the user class"""
        user = User()
        self.assertTrue(hasattr(user, "first_name"))
        self.assertTrue(hasattr(user, "last_name"))
        self.assertTrue(hasattr(user, "email"))
        self.assertTrue(hasattr(user, "password"))
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_input(self):
        """testing the various input for vendor"""
        user = User()
        user.email = "peterjohn@mail.com"
        user.password = "root"
        user.first_name = "peter"
        user.last_name = "john"

        self.assertEqual(user.email, "peterjohn@mail.com")
        self.assertEqual(user.password, "root")
        self.assertEqual(user.first_name, "peter")
        self.assertEqual(user.last_name, "john")
