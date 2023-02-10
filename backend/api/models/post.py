from typing import Optional

from pydantic import BaseModel
from fastapi import UploadFile


class Post(BaseModel):
    caption: Optional[str]
    files: UploadFile
