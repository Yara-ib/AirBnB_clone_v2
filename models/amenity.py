#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, relationship
from models.base_model import Column, String, Table, ForeignKey


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column(
        'place_id', String(60),
        ForeignKey('places.id'),
        nullable=False, primary_key=True
        ),
    Column(
        'amenities.id', String(60),
        ForeignKey('amenities.id'),
        nullable=False, primary_key=True
        )
    )


class Amenity(BaseModel, Base):
    """ Class Amenity"""
    __tablename__ = 'amenities'

    name = Column('name', String(128), nullable=False)

    place_amenities = relationship(
        'Place', secondary='place_amenity',
        viewonly=False, back_populates='amenities'
        )
