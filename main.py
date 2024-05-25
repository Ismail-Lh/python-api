from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World from another file!!!!"}


@app.get("/posts")
def get_all_posts():
    return {"posts": ["post1", "post2", "post3"]}


@app.post("/posts")
def create_post(body: dict = Body(...)):
    return {"message": f"Post with title {body["title"]} was created successfully!"}
