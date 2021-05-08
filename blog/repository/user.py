from sqlalchemy.orm import Session
from .. import schemas,models
from fastapi import HTTPException,status
from ..models import Role
from enum import Enum

def show_all(db:Session):
    users = db.query(models.User).all()
    return users


def create(db:Session,name:str,email:str,password:str,role:str,url:str,):
    new_user = models.User(name = name,email = email,password =password,role = role,url = url)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def delete(id:int,db:Session,get_current_user:schemas.User):
    if get_current_user.role == "User":
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found ")
        if user.role == "Admin":
            return "You can't delete Admin"
        else:
            user.delete(synchronize_session=False)
            db.commit()
            return f"User with id {id} id deleted"
    else:
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found ")
        user.delete(synchronize_session=False)
        db.commit()
        return 'Delete'

def update(id:int,db:Session,get_current_user:schemas.User):
    if get_current_user.role == "User":
        user = db.query(models.User).filter(models.User.id == id).first()
        if user.role == "Admin":
            return "User can't change admin data"
        else:
            db.update(user)
            db.commit()
            return 'Done'
    else:
        user=db.query(models.User).filter(models.User.id == id).first()
        user.update(request)
        db.commit()
        return 'Record updated'

def show(id:int,db:Session,get_current_user:schemas.User):
    if get_current_user.role == "User":
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"The user of id {id} is not found")
        if user.role == "Admin":
            return "User can't access Admin data"
        return user
    else:
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"The user of id {id} is not found")
        return user