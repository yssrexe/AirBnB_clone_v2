#!/usr/bin/python3
"""_summary_"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv

from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """_summary_"""
    __engine = None
    __session = None

    def __init__(self):
        """_summary_
        """
        user = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{password}@{host}/{db_name}',
            pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop.all(self.__engine)

    def all(self, cls=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        classes = [State, City, User, Place, Review, Amenity]
        objects = {}
        if cls:
            classes = [cls]
        for classname in classes:
            objs = self.__session.query(classname).all()
            for obj in objs:
                objects[f"{type(obj).__name__}.{obj.id}"] = obj

        return objects

    def new(self, obj):
        """adds a new obj to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an obj from the database"""
        if obj is None:
            return
        self.__session.delete(obj)

    def reload(self):
        """Crates all tables at the database and start a new session"""

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """removes the scoped session"""
        self.__session.close()
