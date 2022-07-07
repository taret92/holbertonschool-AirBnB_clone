#!/usr/bin/python3
""" Module with Unittest for the BaseModel class.
    """
import inspect
import json
import os
import unittest
import uuid

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Testing the BaseModel class of the program.
        """

    @classmethod
    def setUp(cls):
        """ Method to prepare each single test.
            """
        cls.base_test = BaseModel()
        if os.path.exists("file.json"):
            os.rename("file.json", "original_file.json")

    def test_module_documentation(self):
        """ Test if BaseModel module is documented.
            """
        self.assertTrue(BaseModel.__doc__)

    def test_class_documentation(self):
        """ Test if BaseModel class is documented.
            """
        self.assertTrue(BaseModel.__doc__)

    def test_methods_documentation(self):
        """ Test if all BaseModel methods are documented.
            """
        methods = inspect.getmembers(BaseModel)
        for method in methods:
            self.assertTrue(inspect.getdoc(method))

    def test_basic_base_assigment(self):
        """ Create some basic BaseModel instances.
            """
        self.assertIsInstance(self.base_test, BaseModel)
        self.assertTrue(hasattr(self.base_test, "id"))
        self.assertTrue(hasattr(self.base_test, "created_at"))
        self.assertTrue(hasattr(self.base_test, "updated_at"))

    def test_base_id_assigment(self):
        """ Test if the id of the instance is UUID v4.
            """
        uuid_v4 = uuid.UUID(self.base_test.id, version=4)
        self.assertEqual(str(uuid_v4), self.base_test.id)

    def test_base_assigment_arguments(self):
        """ Test BaseModel instance assigment with arguments.
            """
        self.base_test.name = "I'm a BaseModel"
        self.assertTrue(hasattr(self.base_test, "name"))
        self.assertEqual(self.base_test.to_dict()["name"], "I'm a BaseModel")

    def test_save_method(self):
        """ Check the save() method.
            """
        self.base_test.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json") as file_opened:
            file_dict = json.load(file_opened)
        self.assertTrue(self.base_test.to_dict() in file_dict.values())

    def test_to_dict_method(self):
        """ Check the to_dict() method.
            """
        obj_as_dict = self.base_test.to_dict()
        self.assertEqual(self.base_test.id, obj_as_dict["id"])

    def test_str_method(self):
        """ Check the __str__() method.
            """
        base_fstr = "[{}] ({}) {}".format(self.base_test.__class__.__name__,
                                          self.base_test.id,
                                          self.base_test.__dict__)
        base_srt = self.base_test.__str__()
        self.assertEqual(base_fstr, base_srt)

    def tearDown(self):
        """ Method to leave each test
            """
        if os.path.exists("file.json"):
            os.remove("file.json")
        if os.path.exists("original_file.json"):
            os.rename("original_file.json", "file.json")
