#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
# import sqlalchemy modules
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list


class State(BaseModel, Base):

    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    # write a code to make BaseModel column order first in the table

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    # write a code to make BaseModel column order first in the table

    @property
    def cities(self):
        """getter attribute cities that returns the list of City objects
        from storage linked to the current State"""
        from models import storage
        from models.city import City
        cities = []
        for key, value in storage.all(City).items():
            if value.state_id == self.id:
                cities.append(value)
        return cities
