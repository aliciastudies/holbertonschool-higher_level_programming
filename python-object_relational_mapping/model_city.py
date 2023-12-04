#!/usr/bin/python3
""" contains class definitions of a State and an instance Base """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ create class City & inherits Base """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship(State, backref='cities')

    def __str__(self):
        """
        returns string representation of City object.
        """
        return "{}: ({}) {}".format(self.state.name, self.id, self.name)