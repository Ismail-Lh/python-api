from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: float | None = None


@app.get("/")
def root():
    return {"message": "Hello World from another file!!!!"}


@app.get("/posts")
def get_all_posts():
    return {"posts": ["post1", "post2", "post3"]}


@app.post("/posts")
def create_post(post: Post):
    message = f"Post with title {post.title} was created successfully!"

    return {"data": post.model_dump(), "message": message}
