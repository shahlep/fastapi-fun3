from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str


@app.get("/")
def get_all_post():
    return {"message": "Hello World"}

@app.get("/post/{id}")
def get_post_by_id(id: int):
    pass

@app.post("/posts")
def create_post(post: Post):
    return {"data": post}


@app.put("/post/{id}")
def update_a_post(id: int):
    pass


@app.delete("/post/{id}")
def update_a_post(id: int):
    pass
