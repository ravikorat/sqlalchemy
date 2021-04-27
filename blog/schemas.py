from pydantic import BaseModel
from typing import List,Optional
from .database import Base

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
    
class showUser(BaseModel):
    id : int
    name :str
    email :str
    class Config(): 
        orm_mode = True

class ShowBlog(BaseModel):
    id : int
    title : str
    body : str
    class Config(): 
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email : Optional[str] = None






