#!/usr/bin/python3
# unittest for the base model
"""This tests cases are for the base model class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """the basemodel test cases"""

    def test___init__(self):
        """tests the init method"""
        new_guy = BaseModel()
        new_guy.name = "the first"
        new_guy.my_number = "1"
        another_guy = BaseModel(**(new_guy.to_dict()))
        self.assertEqual(new_guy.id, another_guy.id)

    def test_to_dict(self):
        """tests the to_dict instance method"""
        some_inst = BaseModel()
        dic = some_inst.to_dict()
        self.assertEqual(type(dic).__name__, "dict")
        self.assertIn('created_at', dic)
        self.assertIn('updated_at', dic)
        self.assertEqual(dic['__class__'], 'BaseModel')
        some_inst = BaseModel(**dic)
        self.assertEqual(dic['id'], some_inst.to_dict()['id'])

    def test_save(self):
        """checks that the save method changes the updated time"""
        some_inst = BaseModel()
        some_inst.save()
        created_at = some_inst.created_at
        updated_at = some_inst.updated_at
        self.assertNotEqual(created_at, updated_at)

    def test__str__(self):
        """checks that the str method is fine"""
        thisinst = BaseModel()
