from fastapi import FastAPI ,HTTPException,status
from pydantic import BaseModel
from typing import Optional
from random import randrange


app=FastAPI()


#pydantic model
class post(BaseModel):
    title:str
    content:str
    published:str
    rating:Optional[int]=None



def getpost(id):
    for p in db:
        if p['id']==id:
            return p


def find_post(id):
    for i,p in enumerate(db):
        if p["id"]==id:
            return i


db=[{"title":"1st title","content":"1st content","published":"1st user","id":1}]

@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(data:post):
    datadict=data.model_dump()
    datadict['id']=randrange(1,1000)
    db.append(datadict)
    return {"msg":"successfully created post","name":datadict}


@app.get("/posts")
def get_posts():
    return db

@app.get("/posts/latest")
def get_latest_posts():
    posts=db[len(db)-1]
    return posts

@app.get("/posts/{id}")
def get_post(id:int):
    post=getpost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found ")
    return {"data":post}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    index=find_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id :{id} doesnt exist')
    db.pop(index)
    return {"msg":"post sucessfully deleted"}

@app.put("/posts/{id}")
def update_post(data:post,id:int):
    index=find_post(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id :{id} doesnt exist')
    db.pop(index)
    datadict=data.model_dump()
    datadict['id']=randrange(1,1000)
    db.append(datadict)
    return {"msg":"sucessfully updated post"}

