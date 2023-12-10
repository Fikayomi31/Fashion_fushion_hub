#!/usr/bin/python3
"""Module contain test class for console"""

import unittest
import pycodestyle
import inspect
import console
FFHCommand = console.FFHCommand
console_doc = console.FFHCommand.__doc__


class TestConsoleDocs(unittest.TestCase):
    """Test to check for documentation and style of console"""

    def test_pycodestyle_conformance(self):
        """Test that console conforms with pep8"""
        for path in ['console.py',
                     'tests/test_console.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for module docstring"""
        self.assertIsNot(console_doc, None,
                         'console.py needs a docstring')
        self.assertTrue(len(console_doc) > 1,
                        'console.py needs a docstring')

    def test_class_docstring(self):
        """Test for FFHCommand class docstring"""
        self.assertIsNot(FFHCommand.__doc__, None,
                         'FFHCommand class needs a docstring')
        self.assertTrue(len(FFHCommand.__doc__) >= 1,
                        'FFHCommand class needs a docstring')
