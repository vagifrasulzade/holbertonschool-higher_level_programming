#!/usr/bin/python3
"""SqlAlchemy model for the cities table"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """SqlAlchemy model for the cities table"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
