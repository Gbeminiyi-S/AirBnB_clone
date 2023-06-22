#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

        # To test reinitialisation of instance of the dictionary
        base_model_dict = base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertNotEqual(base_model, new_base_model)
        self.assertEqual(base_model.id, new_base_model.id)
        self.assertEqual(base_model.created_at, new_base_model.created_at)
        self.assertEqual(base_model.updated_at, new_base_model.updated_at)
        self.assertNotIn('__class__', new_base_model.__dict__)

    def test_str_method(self):
        base_model = BaseModel()
        class_name = base_model.__class__.__name__
        dic = base_model.__dict__
        expected_output = "[{}] ({}) {}".format(class_name, base_model.id, dic)

        self.assertEqual(str(base_model), expected_output)

    def test_save_method(self):
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at

        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_method(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        new_created_at = base_model.created_at.isoformat()
        new_updated_at = base_model.updated_at.isoformat()

        self.assertIsInstance(base_model_dict, dict)
        self.assertEqual(base_model_dict['__class__'], 'BaseModel')
        self.assertEqual(base_model_dict['id'], base_model.id)
        self.assertEqual(base_model_dict['created_at'], new_created_at)
        self.assertEqual(base_model_dict['updated_at'], new_updated_at)


if __name__ == '__main__':
    unittest.main()
