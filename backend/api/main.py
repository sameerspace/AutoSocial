import io
from typing import Optional
import aiofiles

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.middleware.cors import CORSMiddleware


from models.post import Post
from instagram import post_to_instagram


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://192.168.18.4:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"message": "Hello World"}


# async def save_image(filename, uploaded_file: UploadFile):
#     async with aiofiles.open(filename, 'wb') as file:
#         content = await uploaded_file.read()
#         await file.write(content)


@app.post("/post_image")
async def post_image(files: list[UploadFile] = File(...), caption: str = Form(...)):
    images: list = []
    for file in files:
        images.append(file)

    post = Post(caption=caption, files=images)

    if post_to_instagram(post=post):
        return {
            "status": "success"
        }

    return {
        "post": post.caption,
        "images": len(post.files)
    }
