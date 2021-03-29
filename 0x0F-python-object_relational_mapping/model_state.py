#!/usr/bin/python3
from sqlalchemy import Column, String, Integer
from sqllchemy.extdeclarative import declarative_base

base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=true, nullable=False)
    name = Column(String(128), nullable=False)
