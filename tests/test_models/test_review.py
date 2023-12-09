#!/usr/bin/python3
"""Defining the test case for Review class"""

from models.review import (Review, BaseModel)
import unittest
import pycodestyle
import time
import inspect
import models
Review = models.review.Review
review_doc = models.review.__doc__


class TestReviewDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that review conforms with pep8"""
        for path in ['models/user.py',
                     'tests/test_models/test_review.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(review_doc, None,
                         'review.py needs a docstring')
        self.assertTrue(len(review_doc) > 1,
                        'review.py needs a docstring')

    def test_class_docstring(self):
        """Test for Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         'Review needs a docstring')
        self.assertTrue(len(Review.__doc__) >= 1,
                        'Review needs a docstring')


class TestReview(unittest.TestCase):
    """test representation for Review"""

    def test_user_id(self):
        """testing for user_id attribute for review model"""
        review = Review()
        self.assertTrue(review, "user_id")
        self.assertEqual(review.user_id, "")
        self.assertEqual(type(review.user_id), str)

    def test_product_id(self):
        """Testing for product_id attribute for review model"""
        review = Review()
        self.assertTrue(review, "product_id")
        self.assertEqual(review.product_id, "")
        self.assertEqual(type(review.product_id), str)

    def test_text(self):
        """Testing for text attributes for review model"""
        review = Review()
        self.assertTrue(review, "text")
        self.assertEqual(review.text, "")
        self.assertEqual(type(review.text), str)

    def test_attribute(self):
        """Testing for the attribute of all the review class"""
        review = Review()
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "product_id"))
        self.assertTrue(hasattr(review, "text"))
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_input(self):
        """testing the various input for vendor"""
        review = Review()
        review.user_id = "01"
        review.product_id = "11"
        review.text = "bad_product"
        self.assertEqual(review.user_id, "01")
        self.assertEqual(review.product_id, "11")
        self.assertEqual(review.text, "bad_product")
