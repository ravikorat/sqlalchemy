from fastapi import APIRouter,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas,database,models,hashing,token,oauth2
from jose import jwt
from blog.hashing import Hash

router = APIRouter(tags = ['Authentication'])
   
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

@router.post('/login')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session = Depends(database.get_db),):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    
    if not user:
        raise HTTPException (status_code = status.HTTP_404_NOT_FOUND,detail = f"Invalid credentials")
    
    # if not Hash.verify(user.password,request.password):
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Incorrect password")

    access_token = token.create_access_token(data={"id":user.id,"sub": user.email,"role":user.role})
    return {"access_token":access_token,"token_type": "bearer"}

