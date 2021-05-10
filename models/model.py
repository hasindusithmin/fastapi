from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:Optional[int] = None
    name:str
    age :int
    email:str
    lang:str
    