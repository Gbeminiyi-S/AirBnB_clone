#!/usr/bin/python3
import unittest
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
import os

def is_string_empty(string):
    return len(string) == 0

class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        user = User()
        self.assertIsInstance(user.id, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

if __name__ == '__main__':
    unittest.main()
