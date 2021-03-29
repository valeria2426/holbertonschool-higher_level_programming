#!/usr/bin/python3
"""
declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """docstring  ."""
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
