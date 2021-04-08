import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True) 
    firstName = Column(String(50))
    lastName = Column(String(50))
    email = Column(String(100))
    picture = Column(String(250))
    user = relationship('Favorite', back_populates="user") 

class Favorite(Base):  
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    date = Column(String(25))
    user_id = Column(Integer, ForeignKey('user.id')) 
    character = relationship('Characters', back_populates="favorite") 
    planet = relationship('Planets', back_populates="favorite") 

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    gender = Column(String(25))
    description = Column(String())
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    population = Column(Integer)
    description = Column(String())
    favorite_id = Column(Integer, ForeignKey('favorite.id'))





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')