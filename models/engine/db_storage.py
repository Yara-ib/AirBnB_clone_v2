#!/usr/bin/python3
""" DBStorage Module """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session

class DBStorage():
    __engine = None
    __session = None

    def __init__(self) -> None:
        self.__engine = create_engine('''
            mysql+mysqldb://
            getenv('HBNB_MYSQL_USER'):
            getenv('HBNB_MYSQL_PWD')
            @getenv('HBNB_MYSQL_HOST')/
            getenv('HBNB_MYSQL_DB')''',
            pool_pre_ping=True
            )

    def all(self, cls=None):
        """ Query on the current database session """


    def new(self, obj):
        """ Add the object to the current db session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current db session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            del obj
            self.__session.commit()

    def reload(self):
        """ Finishing the work """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        Base.metadata.create_all(DBStorage.__engine)

        self.__session = sessionmaker(bind=self.__engine,
                         expire_on_commit=False)
        Session = scoped_session(self.__session)
