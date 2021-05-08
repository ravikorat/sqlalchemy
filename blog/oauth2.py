from fastapi import Depends, HTTPException, status,Form
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from . import models, token, schemas
from .database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "login")

def get_current_user(data: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    data_token = token.verify_token(data, credentials_exception)
    user = db.query(models.User).filter(models.User.email == data_token.email).first()
    return user