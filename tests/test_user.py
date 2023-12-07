#!/usr/bin/python3
"""Defining the test case for user class"""

from models.user import (User, BaseModel)
import unittest


class TestUser(unittest.TestCase):
    """test representation for User"""

    def setUp(self):
        """setting up test cases for user"""
        self.user = User()

    def tearDown(self):
        """Deleting the test cases"""
        del self.user

    def test_classattr(self):
        """testing the public class attribute for user model"""
        user = self.user
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        user.email = "peterjohn@mail.com"
        user.password = "root"
        user.first_name = "peter"
        user.last_name = "john"
        self.assertEqual(user.email, "peterjohn@mail.com")
        self.assertEqual(user.password, "root")
        self.assertEqual(user.first_name, "peter")
        self.assertEqual(user.last_name, "john")
