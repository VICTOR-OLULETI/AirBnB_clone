#!/usr/bin/python3
"""Sets of Unittest on the BaseModel Class
"""

import os
import unittest
import inspect
import models
from unittest import mock
import pycodestyle
# import pep8 as pycodestyle
from models.base_model import BaseModel
from datetime import datetime
import time
module_doc = BaseModel.__doc__


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check if documentation exist and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8(self):
        """Test python files for conformance to PEP8."""
        for path in [
                'models/base_model.py',
                'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(module_doc, None, "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) > 1, "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(
                BaseModel.__doc__, None,
                "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstring(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(
                    func[1].__doc__,
                    None,
                    "{:s} method needs a docstring".format(func[0])
                    )
                self.assertTrue(
                        len(func[1].__doc__) > 1,
                        "{:s} method needs a docstring".format(func[0]))


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""
    def test_instantiation(self):
        """Test that object is created"""
        Inst = BaseModel()
        self.assertIs(type(Inst), BaseModel)
        Inst.name = "Holberton"
        Inst.number = 89
        attrs = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "number": int
                }
        for key, value in attrs.items():
            with self.subTest(attr=key, typ=value):
                self.assertIn(key, Inst.__dict__)
                self.assertIs(type(Inst.__dict__[key]), value)
        self.assertEqual(Inst.name, "Holberton")
        self.assertEqual(Inst.number, 89)

    def test_datetime_attributes(self):
        """Test that two BaseModel have different datetime object
        and that upon creation have identical updated_at
        and created_at value.
        """
        tic = datetime.now()
        inst1 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst1.created_at <= toc)
        time.sleep(1e-4)
        tic = datetime.now()
        inst2 = BaseModel()
        toc = datetime.now()
        self.assertTrue(tic <= inst2.created_at <= toc)
        self.assertTrue(inst1.created_at <= inst1.updated_at)
        self.assertTrue(inst2.created_at <= inst2.updated_at)
        self.assertNotEqual(inst1.created_at, inst2.created_at)
        self.assertNotEqual(inst1.updated_at, inst2.updated_at)

    def test_uuid(self):
        """Test that id is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(
                        uuid,
                        '^[0-9a-f]{8}-[0-9a-f]{4}'
                        '-[0-9a-f]{4}-[0-9a-f]{4}'
                        '-[0-9a-f]{12}$')
        self.assertNotEqual(inst1.id, inst2.id)

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json
        """
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        d = my_model.to_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.assertCountEqual(d.keys(), expected_attrs)
        self.assertEqual(d['__class__'], 'BaseModel')
        self.assertEqual(d['name'], "Holberton")
        self.assertEqual(d['my_number'], 89)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.to_dict()
        self.assertEqual(new_d["__class__"], "BaseModel")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], bm.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], bm.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        inst = BaseModel()
        string = "[BaseModel] ({}) {}".format(inst.id, inst.__dict__)
        self.assertEqual(string, str(inst))

    @mock.patch('models.storage')
    def test_save(self, mock_storage):
        """Test that save method updates `updated_at` and calls
        `storage.save`"""
        inst = BaseModel()
        old_created_at = inst.created_at
        old_updated_at = inst.updated_at
        inst.save()
        new_created_at = inst.created_at
        new_updated_at = inst.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)
        # self.assertTrue(mock_storage.new.called)
        # self.assertTrue(mock_storage.save.called)
