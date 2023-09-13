from fastapi import FastAPI ,HTTPException,status,Response
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app=FastAPI()


class post(BaseModel):
    title:str
    content:str
    published:str
    


#database connection [postgresql]
while True:
    try:
        conn=psycopg2.connect(host='localhost', database='fastapi', user='postgres',password='loki@123',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print("DB connection successfull")
        break

    except Exception as err:
        print(f'connection failed : {err}')    
        time.sleep(3)

'''
(PostgreSQL) table :


CREATE TABLE posts
(
    id serial,
    title character varying NOT NULL,
    content character varying NOT NULL,
    published boolean NOT NULL DEFAULT True,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    PRIMARY KEY (id)
);


'''


@app.post("/posts",status_code=status.HTTP_201_CREATED)
def create_post(data:post):
    cursor.execute("""INSERT INTO POSTS(title,content,published) VALUES(%s ,%s ,%s) RETURNING *""",(data.title,data.content,data.published))
    post=cursor.fetchone()
    conn.commit()
    return {"msg":post}


@app.get("/posts")
def get_posts():
    cursor.execute("""select * from posts;""")
    posts=cursor.fetchall()
    return {"data":posts}

@app.get("/posts/latest")
def get_latest_posts():
    cursor.execute("""select * from posts order by id DESC;""")
    posts=cursor.fetchall()
    return {"data":posts}

@app.get("/posts/{id}")
def get_post(id:int):
    cursor.execute("""select * from posts where id = %s""",(str(id),))
    posts=cursor.fetchone()
    if posts==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id:{id} not found ")
    return {"data":posts}


@app.delete("/posts/{id}")
def delete_post(id:int):
    cursor.execute("""delete  from posts where id = %s """,(str(id),))
    if cursor.rowcount == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} doesn't exist."
        )
    conn.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(data:post,id:int):
    cursor.execute("""update posts set title=%s,content =%s,published=%s where id=%s RETURNING *""",(data.title,data.content,data.published,str(id)))
    posts=cursor.fetchone()
    if  posts:
        conn.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'post with id :{id} doesnt exist')
    
    
    return {"data":posts}

