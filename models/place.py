#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String, Integer, relationship
from sqlalchemy import Float, ForeignKey
from models.review import Review
from models.amenity import Amenity
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
if getenv(key='HBNB_TYPE_STORAGE') == 'db':
    __tablename__ = 'places'

    city_id = Column(
        'city_id', String(60),
        ForeignKey('cities.id'), nullable=False
        )

    user_id = Column(
        'user_id', String(60),
        ForeignKey('users.id'), nullable=False
        )

    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024))

    number_rooms = Column('number_rooms', Integer, nullable=False, default=0)

    number_bathrooms = Column(
        'number_bathrooms', Integer,
        nullable=False, default=0
        )

    max_guest = Column('max_guest', Integer, nullable=False, default=0)

    price_by_night = Column(
        'price_by_night', Integer,
        nullable=False, default=0
        )

    latitude = Column('latitude', Float)
    longitude = Column('longitude', Float)

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
    amenity_ids = []

    reviews = relationship('Review', backref='place')

    amenities = relationship(
        'Amenity', secondary='place_amenity',
        viewonly=False, back_populates='place_amenities')

    @property
    def reviews(self):
        """ Getter for reviews """
        reviews_collection = []
        for item in self.reviews:
            if item.place_id == self.id:
                reviews_collection.append(item)
        return reviews_collection

    @property
    def amenities(self):
        """ Getter for amenities """
        amenities_collection = []
        for item in self.amenities:
            if Place.amenity_ids == Amenity.id:
                amenities_collection.append(item)
        return amenities_collection

    @amenities.setter
    def amenities(self, obj):
        """ Setter/Appending values to Amenity_ids list """
        if isinstance(obj, Amenity):
            self.amenity_ids.append(obj.id)
