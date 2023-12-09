#!/usr/bin/python3
"""Module contain test class for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel
import pycodestyle
import time
import inspect
import models
BaseModel = models.base_model.BaseModel
module_doc = models.base_model.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Test to check for documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """set up docstring tests"""
        self.base_func = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pycodestyle_conformance(self):
        """Test that base_model conforms with pep8"""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(module_doc, None,
                         'base_model.py needs a docstring')
        self.assertTrue(len(module_doc) > 1,
                        'base_model.py needs a docstring')

    def test_class_docstring(self):
        """Test for BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         'BaseModel needs a docstring')
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        'BaseModel needs a docstring')


class TestBaseModel(unittest.TestCase):
    """Test Case for BaseModel
    """

    def test_datetime_attributes(self):
        """Test that datetime are different between created_at and
        updated_at and are identical upon creation
        """
        time_1 = datetime.now()
        bm1 = BaseModel()
        time_2 = datetime.now()
        self.assertTrue(time_1 <= bm1.created_at <= time_2)
        time.sleep(1e-4)
        time_1 = datetime.now()
        bm2 = BaseModel()
        time_2 = datetime.now()
        self.assertTrue(time_1 <= bm2.created_at <= time_2)
        self.assertNotEqual(bm1.created_at, bm1.updated_at)
        self.assertNotEqual(bm2.created_at, bm2.updated_at)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_uuid_attributes(self):
        """Test that id is a valid uuid"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        for bm_id in [bm1, bm2]:
            uuid = bm_id.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)

    def test_init_without_kwargs(self):
        """testing init method without kwargs"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_init_with_kwargs(self):
        """testing init method with kwargs"""
        bm3 = BaseModel()
        bm3.name = "test"
        bm3.my_number = 89
        self.assertIsInstance(bm3.id, str)
        self.assertEqual(bm3.name, 'test')
        self.assertIsInstance(bm3.name, str)
        self.assertEqual(bm3.my_number, 89)
        self.assertIsInstance(bm3.my_number, int)

    def test_str(self):
        """Testing str output"""
        bm1 = BaseModel()
        output_str = "[BaseModel] ({}) {}".format(bm1.id, bm1.__dict__)
        self.assertEqual(output_str, str(bm1))

    def test_save(self):
        """Testing for save module"""
        bm1 = BaseModel()
        old_updated_at = bm1.updated_at
        bm1.save()
        self.assertNotEqual(old_updated_at, bm1.updated_at)

    def test_to_dict_value(self):
        """Testing the value of the dict"""
        bm1 = BaseModel()
        bm1_dict = bm1.to_dict()
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm1_dict["created_at"]), str)
        self.assertEqual(type(bm1_dict["updated_at"]), str)
        self.assertEqual(bm1_dict["created_at"], bm1.created_at.isoformat())
        self.assertEqual(bm1_dict["updated_at"], bm1.updated_at.isoformat())

    def test_attributes(self):
        """Testing for the BaseModel class attributes"""
        bm = BaseModel()
        self.assertTrue(hasattr(bm, "id"))
        self.assertTrue(hasattr(bm, "created_at"))
        self.assertTrue(hasattr(bm, "updated_at"))


if __name__ == "__main__":
    unittest.main()
