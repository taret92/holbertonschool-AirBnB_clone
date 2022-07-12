#!/usr/bin/python3
""" Module with Unittest for the Place class.
    """
import inspect
import os
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Testing the Place class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.place_test = Place()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if Place module is documented.
            """
        self.assertTrue(Place.__doc__)

    def test_class_documentation(self):
        """ Test if Place class is documented.
            """
        self.assertTrue(Place.__doc__)

    def test_methods_documentation(self):
        """ Test if all Place methods are documented.
            """
        methods = inspect.getmembers(Place)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Place instances.
            """
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.place_test, Place)
        self.assertTrue(hasattr(self.place_test, "id"))
        self.assertTrue(hasattr(self.place_test, "created_at"))
        self.assertTrue(hasattr(self.place_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Place instance assigment with attributes
            """
        self.assertTrue(hasattr(self.place_test, "city_id"))
        self.assertTrue(hasattr(self.place_test, "user_id"))
        self.assertTrue(hasattr(self.place_test, "name"))
        self.assertTrue(hasattr(self.place_test, "description"))
        self.assertTrue(hasattr(self.place_test, "number_rooms"))
        self.assertTrue(hasattr(self.place_test, "max_guest"))
        self.assertTrue(hasattr(self.place_test, "price_by_night"))
        self.assertTrue(hasattr(self.place_test, "latitude"))
        self.assertTrue(hasattr(self.place_test, "longitude"))
        self.assertTrue(hasattr(self.place_test, "amenity_ids"))
        self.assertIsInstance(self.place_test.city_id, str)
        self.assertIsInstance(self.place_test.user_id, str)
        self.assertIsInstance(self.place_test.name, str)
        self.assertIsInstance(self.place_test.description, str)
        self.assertIsInstance(self.place_test.number_rooms, int)
        self.assertIsInstance(self.place_test.number_bathrooms, int)
        self.assertIsInstance(self.place_test.max_guest, int)
        self.assertIsInstance(self.place_test.price_by_night, int)
        self.assertIsInstance(self.place_test.latitude, float)
        self.assertIsInstance(self.place_test.longitude, float)
        self.assertIsInstance(self.place_test.amenity_ids, list)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
