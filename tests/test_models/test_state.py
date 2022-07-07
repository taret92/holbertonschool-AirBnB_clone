#!/usr/bin/python3
""" Module with Unittest for the State class.
    """

import inspect
import os
import unittest

from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Testing the State class of the program.
        """

    def setUp(self):
        """ Method to prepare each single test.
            """
        self.state_test = State()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if State module is documented.
            """
        self.assertTrue(State.__doc__)

    def test_class_documentation(self):
        """ Test if State class is documented.
            """
        self.assertTrue(State.__doc__)

    def test_methods_documentation(self):
        """ Test if all State methods are documented.
            """
        methods = inspect.getmembers(State)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic State instances.
            """
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state_test, State)
        self.assertTrue(hasattr(self.state_test, "id"))
        self.assertTrue(hasattr(self.state_test, "created_at"))
        self.assertTrue(hasattr(self.state_test, "updated_at"))

    def test_base_assigment_arguments(self):
        """ Test State instance assigment with arguments.
            """
        self.assertTrue(hasattr(self.state_test, "name"))
        self.assertIsInstance(self.state_test.name, str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
