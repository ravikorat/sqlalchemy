from .database import Base
from sqlalchemy import Column ,Integer,String , ForeignKey,Enum
import enum
from sqlalchemy_utils import URLType
from sqlalchemy.orm import relationship
from enum import Enum

class Role(str,Enum):
    Admin = 'Admin'
    User = 'User'

class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    author = relationship("User",back_populates="blogs")

class User(Base):
    __tablename__='users'

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    url = Column(URLType)
    role = Column(String,default=Role.Admin)

    blogs = relationship('Blog',back_populates="author")