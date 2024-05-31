#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City

from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """a getter method for retriving all cities with the same state id

            Returns:
                list: a list of city instances
            """
            cities = list(models.storage.all(City).values())
            return [city for city in cities if city.state_id == self.id]
