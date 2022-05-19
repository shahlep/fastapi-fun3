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


@app.post('/post')
def create_post(post: Post):
    return f'{post.title}  {post.content}'


@app.put('/post/{id}')
def update_a_post(id: int):
    pass


@app.delete('/post/{id}')
def update_a_post(id: int):
    pass
