#!/usr/bin/python3
import unittest
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    def test_instance_attributes(self):
        place = Place()
        self.assertIsInstance(city_id, str)
        self.assertIsInstance(user_id, str)
        self.assertIsInstance(name, str)
        self.assertIsInstance(description, str)
        self.assertIsInstance(number_rooms, int)
        self.assertIsInstance(number_bathrooms, int)
        self.assertIsInstance(max_guest, int)
        self.assertIsInstance(price_by_night, int)
        self.assertIsInstance(latitude, float)
        self.assertIsInstance(longitude, float)
        self.assertIsInstance(amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
