#!/usr/bin/python3
""" Module with Unittest for the City class.
    """
import inspect
import os
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Testing the City class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.city_test = City()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if City module is documented.
            """
        self.assertTrue(City.__doc__)

    def test_class_documentation(self):
        """ Test if City class is documented.
            """
        self.assertTrue(City.__doc__)

    def test_methods_documentation(self):
        """ Test if all City methods are documented.
            """
        methods = inspect.getmembers(City)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic City instances.
            """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city_test, City)
        self.assertTrue(hasattr(self.city_test, "id"))
        self.assertTrue(hasattr(self.city_test, "created_at"))
        self.assertTrue(hasattr(self.city_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test City instance assigment with attributes.
            """
        self.assertTrue(hasattr(self.city_test, "state_id"))
        self.assertTrue(hasattr(self.city_test, "name"))
        self.assertIsInstance(self.city_test.state_id, str)
        self.assertIsInstance(self.city_test.name, str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
