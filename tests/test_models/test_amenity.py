#!/usr/bin/python3
""" Module with Unittest for the Amenity class.
    """

import inspect
import os
import unittest

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ Testing the Amenity class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.amenity_test = Amenity()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if Amenity module is documented.
            """
        self.assertTrue(Amenity.__doc__)

    def test_class_documentation(self):
        """ Test if Amenity class is documented.
            """
        self.assertTrue(Amenity.__doc__)

    def test_methods_documentation(self):
        """ Test if all Amenity methods are documented.
            """
        methods = inspect.getmembers(Amenity)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Amenity instances.
            """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity_test, Amenity)
        self.assertTrue(hasattr(self.amenity_test, "id"))
        self.assertTrue(hasattr(self.amenity_test, "created_at"))
        self.assertTrue(hasattr(self.amenity_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Amenity instance assigment attributes.
            """
        self.assertTrue(hasattr(self.amenity_test, "name"))
        self.assertIsInstance(self.amenity_test.name, str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
