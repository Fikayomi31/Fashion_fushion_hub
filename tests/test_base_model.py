#!/usr/bin/python3
"""Module contain test class for BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test Case for BaseModel
    """

    date_format = "%Y-%m-%dT%H:%M:%S.%f"
    date_string = "2023-12-01T20:29:01.672318"
    date_object = datetime.strptime(date_string, date_format)
    kwargs = {
            'id': '327399',
            'created_at' : date_string,
            'updated_at' : date_string,
            'name': 'test',
            'my_number': 89
            }

    def setUp(self):
        """setting the testing variable"""
        self.bm1 = BaseModel()
        self.bm2 = BaseModel()
        self.bm3 = BaseModel(**self.kwargs)

    def tearDown(self):
        """Deleting the test variable"""
        del self.bm1
        del self.bm2
        del self.bm3

    def test_init_without_kwargs(self):
        """testing init method without kwargs"""
        bm1 = self.bm1
        bm2 = self.bm2
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertNotEqual(bm1.created_at, bm2.created_at)
        self.assertNotEqual(bm1.updated_at, bm2.updated_at)

    def test_init_with_kwargs(self):
        """testing init method with kwargs"""
        bm3 = self.bm3
        self.assertEqual(bm3.id, '327399')
        self.assertIsInstance(bm3.id, str)
        self.assertEqual(bm3.name, 'test')
        self.assertIsInstance(bm3.name, str)
        self.assertEqual(bm3.my_number, 89)
        self.assertIsInstance(bm3.my_number, int)
        self.assertEqual(bm3.created_at, self.date_object)
        self.assertEqual(bm3.updated_at, self.date_object)

    def test_str(self):
        """Testing str output"""
        bm1 = self.bm1
        output_str = "[BaseModel] ({}) {}".format(bm1.id, bm1.__dict__)
        self.assertEqual(output_str, str(bm1))

    def test_save(self):
        """Testing for save module"""
        bm1 = self.bm1
        old_updated_at = bm1.updated_at
        bm1.save()
        self.assertNotEqual(old_updated_at, bm1.updated_at)
    
    def test_to_dict_value(self):
        """Testing the value of the dict"""
        bm1 = self.bm1
        bm1_dict = bm1.to_dict()
        self.assertEqual(bm1_dict["__class__"], "BaseModel")
        self.assertEqual(type(bm1_dict["created_at"]), str)
        self.assertEqual(type(bm1_dict["updated_at"]), str)
        self.assertEqual(bm1_dict["created_at"], bm1.created_at.isoformat())
        self.assertEqual(bm1_dict["updated_at"], bm1.updated_at.isoformat())

    
if __name__ == "__main__":
    unittest.main()
