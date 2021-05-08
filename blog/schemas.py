from pydantic import BaseModel
from typing import List,Optional
from .database import Base
from .models import Role
from sqlalchemy.types import Enum

class BlogBase(BaseModel):
    title : str
    body : str
    class Config(): 
        orm_mode = True

class Blog(BlogBase):
    class Config(): 
        orm_mode = True
    
class User(BaseModel):
    name :str
    email : str
    password : str
    role : Role

    class Config():
        orm_mode = True

class showUser(BaseModel):
    id : int
    name :str
    email :str
    role : Role
    url : str
    
    class Config(): 
        orm_mode = True

class ShowBlog(BaseModel):
    id : int
    title : str
    body : str
    user_id : int
    class Config(): 
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str
    role : Role

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email : Optional[str] = None





