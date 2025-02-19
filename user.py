from app2.Backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable
from app2.Models import *

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')

print(CreateTable(User.__table__))
