#/usr/bin/python3
# Write a file that contains class defns os a state and an instance
# Base =  delcarative_base()
# State class:
# inherits from base class, link to MySQL table 'state',
# has column id and name
# Must use SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
