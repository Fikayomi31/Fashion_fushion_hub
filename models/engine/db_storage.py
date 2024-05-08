#!/usr/bin/python3
"""Class to manage file storage for ffh clone"""
from models.base_model import Base
from models.brand import Brand
from models.category import Category
from models.order import Order
from models.review import Review
from models.user import User
from models.product import Product
from models.order_item import OrderItem
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of the class"""
        fh_user = getenv("FFH_MYSQL_USER")
        fh_pwd = getenv("FFH_MYSQL_PWD")
        fh_host = getenv("FFH_MYSQL_HOST")
        fh_db = getenv("FFH_MYSQL_DB")
        fh_env = getenv("FFH_ENV")

        self.__engine = create_engine(
            f"mysql+mysqldb://{fh_user}:{fh_pwd}@{fh_host}/{fh_db}",
            pool_pre_ping=True
        )
        if fh_env == "test":
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        """Reload method"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def all(self, cls=None, id=None):
        """Query all classes or specific one by ID"""
        all_classes = [User, Category, Brand, Order, Product, Review, OrderItem]
        result = {}
        if cls is not None:
            if id is not None:
                obj = self.__session.query(cls).get(id)
                if obj is not None:
                    ClassName = obj.__class__.__name__
                    key_name = ClassName + "." + str(obj.id)
                    result[key_name] = obj
            else:
                for obj in self.__session.query(cls).all():
                    ClassName = obj.__class__.__name__
                    key_name = ClassName + "." + str(obj.id)
                    result[key_name] = obj
        else:
            for clss in allClasses:
                if id is not None:
                    obj = self.__session.query(clss).get(id)
                    if obj is not None:
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
                else:
                    for obj in self.__session.query(clss).all():
                        ClassName = obj.__class__.__name__
                        keyName = ClassName + "." + str(obj.id)
                        result[keyName] = obj
        return result
    
    def search(self, cls, id):
        """ def doc """
        data = self.all(cls)

    def new(self, obj):
        """add new obj"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """doc meth"""
        self.__session.close()