#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenities = relationship("Amenity",
                             secondary=place_amenity,
                             viewonly=False,
                             back_populates="place_amenities"
                             )
    reviews = relationship('Review', cascade="all,delete", backref="place")
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """_summary_

            Returns:
                _type_: _description_
            """
            revs = list(models.storage.all(Review).values())
            return [rev for rev in revs if rev.place_id == self.id]

        @property
        def amenities(self):
            """_summary_

            Returns:
                _type_: _description_
            """
            amenities = list(models.storage.all(Amenity).values())
            return [a for a in amenities if a.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            """_summary_

            Args:
                value (_type_): _description_
            """
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
