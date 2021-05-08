from fastapi import APIRouter,Depends,status,HTTPException,File ,UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from .. import models,schemas,database,hashing,oauth2
# from blog.hashing import Hash
import shutil
from ..repository import user
from enum import Enum


get_db =database.get_db
#instance
router = APIRouter(
    tags=['User'],
    prefix='/user'
)


@router.get('/',response_model=List[schemas.showUser])
def all(db:Session=Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    if get_current_user.role == "User":
        users = db.query(models.User).filter(models.User.role == "User").all()
        return users
    else:
        return user.show_all(db)
    
@router.post('/')
def create(name:str,email:str,password:str,role:str,file:UploadFile = File(...), db:Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    if get_current_user.role == "User":
        return "You can't access this site"
    else:
        with open("media/"+file.filename,"wb") as image:
            shutil.copyfileobj(file.file,image)
 
        url = str("media/"+file.filename)
        return user.create(db=db,name=name,email=email,password=password,role=role,url=url)

@router.delete('/{id}')
def delete(id : int,db:Session=Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.delete(id,db,get_current_user)

@router.put('/{id}',response_model=schemas.User)
def update(id:int,request:schemas.User,db:Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.update(id,db,get_current_user)

@router.get('/{id}',response_model = schemas.showUser)
def show(id:int,db:Session=Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.show(id,db,get_current_user)