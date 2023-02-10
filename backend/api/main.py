import io
from typing import Optional

from fastapi import FastAPI, File, Form
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image

from models.post import Post

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


@app.post("/post_instagram")
async def post_instagram(file: bytes = File(...), caption: str = Form(...)):
    img = Image.open(io.BytesIO(file))
    return {
        'name': img.height,
        'caption': caption,
    }


@app.post("/post_image")
async def post_image(files: list[bytes] = File(...), caption: str = Form(...)):
    print(files)
    images: list = []
    for file in files:
        images.append(Image.open(io.BytesIO(file)))
    return {
        "caption": caption,
        "files_captured": len(images),
    }
