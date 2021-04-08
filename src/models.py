import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) 
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(100))
    picture = Column(String(250))
    user = relationship('Favorite', back_populates="user") # One to Many

class Favorite(Base):  # As every element on the list of favorites
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    date = Column(String(25))
    user_id = Column(Integer, ForeignKey('user.id')) 
    character = relationship('Character', back_populates="favorite") # One to Many
    planet = relationship('Planet', back_populates="favorite") # One to Many

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    birthYear = Column(String(25))
    gender = Column(String(25))
    description = Column(String(300))
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)
    terrain = Column(String(25))
    climate = Column(String(25))
    description = Column(String(300))
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

#------------
#------------
#------------

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')