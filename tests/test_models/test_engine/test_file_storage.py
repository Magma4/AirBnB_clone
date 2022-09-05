#!/usr/bin/python3
"""this module unittests the file storage abstraction
and all other functions implemented
"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json


class TestFileStorage(unittest.TestCase):
    """unittests all the functions in the filestorage class"""

    def test_all(self):
        if os.path.exists("file.json"):
            os.remove("file.json")
        thisobject = BaseModel()
        thisobject.my_number = 98
        thisobject.name = "My Base Model"
        id = thisobject.id
        name = thisobject.name
        create_time = thisobject.created_at
        thisobject.save()
        self.assertEqual(os.path.exists("file.json"), True)
        with open("file.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertEqual(type(json.loads(content)).__name__, 'dict')

    def test_new(self):
        """this checks if after created a new instance,
        it is added to our filestorage upon saving
        """
        if os.path.exists("file.json"):
            os.remove("file.json")
        another = BaseModel()
        another.name = "My second model"
        another.my_number = 90
        another.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_save(self):
        """tests that the save function works as expected"""
        if os.path.exists("file.json"):
            os.remove("file.json")
        another = BaseModel()
        another.name = "My third model"
        another.my_number = 90
        another.save()
        self.assertEqual(os.path.exists("file.json"), True)

    def test_reload(self):
        """this tests the reload function"""
        storage = FileStorage()
        another = BaseModel()
        another.name = "My first model"
        another.my_number = 90
        another.save()
        storage.reload()
        if os.path.exists("file.json"):
            os.remove("file.json")
        thisother = BaseModel()
        thisother.my_number = 90
        thisother.name = "My second model"
        self.assertEqual(os.path.exists("file.json"), False)
