#!/usr/bin/python3
import unittest
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        review = Review()
        self.assertIsInstance(place_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(text, str)


if __name__ == '__main__':
    unittest.main()
