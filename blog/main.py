from fastapi import FastAPI
from . import database
# from database import Base,engine
from .routers import user,blog,authentication


get_db =database.get_db
#instance
app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)






