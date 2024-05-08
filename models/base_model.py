#!/usr/bin/python3
"""Defining a class for baseclass"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Datetime

Base = declarative_base()


class BaseModel:
    """Representation of base class"""
    id = Column(String(60), nullable=False,
                primary_key=True, unique=True)
    created_at = Column(Datetime, nullable=False,
                        default=datetime.datetime.utcnow)
    updated_at = Column(Datetime, nullable=False,
                        default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """initialization of basemodel object from kwargs
        Args:
            *args: None
            **kwargs: a key pair valje of dict created
        """
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, date_format)
                if key != "__class__":
                    setattr(self, key, value)

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return the str representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        if '_sa_instance_state' in new_dict:
            del new_dict['_sa_instance_state']
        return new_dict

    def delete(self):
        """Delete the current instance from the storage"""
        from models import storage
        storage.delete(self)
