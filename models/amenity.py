#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.base_model import Column, String, Table, ForeignKey, relationship


class Amenity(BaseModel, Base):
    """ Class Amenity"""
    __tablename__ = 'amenities'

    name = Column('name', String(128), nullable=False)

    place_amenities = relationship(
        'Place', secondary='place_amenity',
        back_populates='amenities'
        )
