#!/usr/bin/python3
""" Module with Unittest for the Review class.
    """
import inspect
import os
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Testing the Review class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.review_test = Review()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if Review module is documented.
            """
        self.assertTrue(Review.__doc__)

    def test_class_documentation(self):
        """ Test if Review class is documented.
            """
        self.assertTrue(Review.__doc__)

    def test_methods_documentation(self):
        """ Test if all Review methods are documented.
            """
        methods = inspect.getmembers(Review)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic Review instances.
            """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review_test, Review)
        self.assertTrue(hasattr(self.review_test, "id"))
        self.assertTrue(hasattr(self.review_test, "created_at"))
        self.assertTrue(hasattr(self.review_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test Review instance assigment attributes.
            """
        self.assertTrue(hasattr(self.review_test, "place_id"))
        self.assertTrue(hasattr(self.review_test, "user_id"))
        self.assertTrue(hasattr(self.review_test, "text"))
        self.assertIsInstance(self.review_test.place_id, str)
        self.assertIsInstance(self.review_test.user_id, str)
        self.assertIsInstance(self.review_test.text, str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
