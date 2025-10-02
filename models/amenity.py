#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from models.place import place_amenity


class Amenity(BaseModel, Base):

    """Amenity class to store amenity information"""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")

    # def __init__(self, *args, **kwargs):
    #     """initializes amenity"""
    #     super().__init__(*args, **kwargs)
