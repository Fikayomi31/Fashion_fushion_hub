#!/usr/bin/python3
"""Defining the test class for file storage"""
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.brand import Vendor
from models.category import Category
from models.product import Product
from models.order import Order
from models.order_item import OrderItem
from models.review import Review
import models
import inspect
import json
import pycodestyle
import unittest
FileStorage = models.engine.file_storage.FileStorage
filestorage_doc = models.engine.file_storage.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Test to check for documentation and style of FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """set up docstring tests"""
        cls.filestorage_f = inspect.getmembers(FileStorage, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that file_storage conforms with pep8"""
        for path in ['models/engine/file_storage.py',
                     'tests/test_models/test_engine/test_file_storage.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(filestorage_doc, None,
                         'file_storage.py needs a docstring')
        self.assertTrue(len(filestorage_doc) > 1,
                        'file_storage.py needs a docstring')

    def test_class_docstring(self):
        """Test for File Storage class docstring"""
        self.assertIsNot(FileStorage.__doc__, None,
                         'FikeStorage needs a docstring')
        self.assertTrue(len(FileStorage.__doc__) >= 1,
                        'FileStorage needs a docstring')


class TestFileStorage(unittest.TestCase):
    """Test representation of FileStorage"""

    def test_all(self):
        """Testing the all return dict"""
        storage = FileStorage()
        new_dict = storage.all()
        self.assertEqual(type(new_dict), dict)
        self.assertNotEqual(new_dict, {})
        self.assertIs(new_dict, storage._FileStorage__objects)

    def test_new(self):
        """Test the new add object to file storage"""
        storage = FileStorage()
        new_obj = BaseModel()
        storage.new(new_obj)
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertIn(key, storage.all())

    def test_save(self):
        """Test the save to save to file storage"""
        storage = FileStorage()
        new_obj = BaseModel()
        storage.new(new_obj)
        storage.save()
        with open(storage._FileStorage__file_path, 'r') as f:
            content = f.read()
            key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
            self.assertIn(key, content)

    def test_reload(self):
        """Test the file reload of file storage"""
        storage = FileStorage()
        new_obj = BaseModel()
        storage.new(new_obj)
        storage.save()
        storage.reload()
        key = "{}.{}".format(new_obj.__class__.__name__, new_obj.id)
        self.assertIn(key, storage.all())
