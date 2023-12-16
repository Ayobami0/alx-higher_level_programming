#!/usr/bin/python3
"""
The classes for SQLAlchemy tables.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Base clase for the state table in the orm.
    Properties:
        id: Identifier for each state, Int, Not Null
        name: Name of the state, Str, Not Null
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
