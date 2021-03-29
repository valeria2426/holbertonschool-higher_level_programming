#!/usr/bin/python3
'''
contains
'''
from sqlallchemy import Column, Integer, String, foreignKey
from sqlalchemy.ext declarative import declarative_base
from model_state import Base, State


class City(Base):
    ''' emty class '''
    ___tablename___ = 'cities'
    id = colum(Integer, primary_key=true, nullable=false)
    name = colum(String(128), nullable=false)
    state_id = column(Integer, forignkey('states.id'), nullable=false)
