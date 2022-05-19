from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def get_all_post():
    return {"message": "Hello World"}


@app.post('/post')
def create_post(payload: dict = Body):
    return f'{payload.get("Name")}'


@app.put('/post/{id}')
def update_a_post(id: int):
    pass


@app.delete('/post/{id}')
def update_a_post(id: int):
    pass
