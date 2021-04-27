from fastapi import FastAPI
from . import database
# from database import Base,engine
from .routers import user,blog,authentication


get_db =database.get_db
#instance
app = FastAPI()

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)



# @app.get('/user',response_model=schemas.showUser)
# def showAll(db:Session=Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.post('/user',response_model=schemas.showUser)
# def create(request:schemas.User, db:Session = Depends(get_db)):
#     new_user = models.User(name = request.name,email = request.email,password = request.password)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.delete('/user/{id}')
# def destroy(id : int,db:Session=Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id)
#     if not user.first():
#         raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found ")
#     user.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put('/user/{id}')
# def update(id:int,request:schemas.User,db:Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"User with id {id} is not found")
#     user.update(request)
#     db.commit()
#     db.refresh(user)
#     return 'done'








