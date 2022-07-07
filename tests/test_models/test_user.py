#!/usr/bin/python3
""" Module with Unittest for the User class.
    """
import inspect
import os
import unittest

from models.user import User


class TestUser(unittest.TestCase):
    """ Testing the User class of the program.
        """

    def setUp(self):
        """ Method to initializate each test
            """
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if User module is documented.
            """
        self.assertTrue(User.__doc__)

    def test_class_documentation(self):
        """ Test if User class is documented.
            """
        self.assertTrue(User.__doc__)

    def test_methods_documentation(self):
        """ Test if all User methods are documented.
            """
        methods = inspect.getmembers(User)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic User instances.
            """
        user_test = User()
        self.assertIsInstance(user_test, User)
        self.assertTrue(hasattr(user_test, "id"))
        self.assertTrue(hasattr(user_test, "created_at"))
        self.assertTrue(hasattr(user_test, "updated_at"))

    def test_base_assigment_attributes(self):
        """ Test User instance assigment attributes.
            """
        user_test = User()
        self.assertTrue(hasattr(user_test, "email"))
        self.assertEqual(user_test.email, "")
        self.assertTrue(hasattr(user_test, "password"))
        self.assertEqual(user_test.password, "")
        self.assertTrue(hasattr(user_test, "first_name"))
        self.assertEqual(user_test.first_name, "")
        self.assertTrue(hasattr(user_test, "last_name"))
        self.assertEqual(user_test.last_name, "")

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        user_test = User()
        user_as_dict = user_test.to_dict()
        self.assertIsInstance(user_as_dict, dict)
        self.assertEqual(user_test.id, user_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        user_test = User()
        user_fstr = "[{}] ({}) {}".format(user_test.__class__.__name__,
                                          user_test.id, user_test.__dict__)
        user_str = user_test.__str__()
        self.assertEqual(user_fstr, user_str)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
