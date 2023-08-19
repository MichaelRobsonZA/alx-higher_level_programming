#!/usr/bin/python3
"""Defines a State class and creates an instance of declarative_base"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class representation of a state"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    def __str__(self):
        """String representation of the State instance"""
        return "{}: {}".format(self.id, self.name)
