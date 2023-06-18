#!/usr/bin/python3
"""This Module creates the class BaseModel"""
import uuid
import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """prints an instance of the object specified"""
        className = self.__class__.__name__
        selfId = self.id
        selfDict = self.__dict__

        return "[{}] ({}) {}".format(className, selfId, selfDict)

    def save(self):
        """updates the `updated_at` attribute with current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
           of the instance
        """
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({"__class__": self.__class__.__name__})
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary
