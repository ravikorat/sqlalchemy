from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import models,schemas,database,hashing
# from blog.hashing import Hash


get_db =database.get_db
#instance
router = APIRouter(
    tags=['User'],
    prefix='/user'
)


@router.get('/',response_model=List[schemas.showUser])
def all(db:Session=Depends(get_db)):
    users = db.query(models.User).all()
    return users



@router.post('/')
def create(request:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name = request.name,email = request.email,password =hashing.Hash.bcrypt(request.password) )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.delete('/{id}')
def delete(id : int,db:Session=Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found ")
    user.delete(synchronize_session=False)
    db.commit()
    return 'Done'

@router.put('/{id}',response_model=schemas.User)
def update(id:int,request:schemas.User,db:Session = Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == id).first()
    user.update(request)
    db.commit()
    return 'Done'