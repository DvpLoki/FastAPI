from fastapi import FastAPI 

from . import Models 
from .Database import engine
from .routes import post,user,Auth

Models.Base.metadata.create_all(bind=engine)


app=FastAPI()

app.include_router(post.app)
app.include_router(user.app)
app.include_router(Auth.app)