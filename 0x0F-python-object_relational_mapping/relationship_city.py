#!/usr/bin/python3
"""
The classes for SQLAlchemy tables.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class City(Base):
    """
    Base clase for the city table in the orm.
    Properties:
        id: Identifier for each City, Int, Not Null
        name: Name of the City, Str, Not Null
        states_id: id of the state at which the city is in
            Int, Not Null, ForeignKey
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
