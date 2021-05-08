from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.orm import Session
from .. import models,schemas,database,oauth2,token


get_db =database.get_db
router=APIRouter(
    tags=['Blog'],
    prefix='/blog'
)

@router.get('/',response_model = List[schemas.ShowBlog])
def all(db:Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/')
def create(request:OAuth2PasswordRequestForm=Depends(schemas.Blog),
            db:Session = Depends(get_db),
            get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title = request.title,body = request.body,user_id = get_current_user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.delete('/{id}')
def delete(id:int,request:schemas.Blog,db:Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail = f"The blog of id {id} is not found")
    blog.delete(synchronize_session = False)
    db.commit()
    return f"Deleted the record of id {id}"

@router.put('/{id}')
def update(id:int,request:schemas.Blog,db:Session = Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog=db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"The blog of id {id} is not found")
    blog.update(request)
    db.commit()
    return "Done"

@router.get('/{id}',response_model = schemas.ShowBlog)
def show(id:int,db:Session=Depends(get_db),get_current_user:schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"The blog of id {id} is not found")
    return blog 