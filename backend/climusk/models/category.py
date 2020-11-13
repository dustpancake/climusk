from pydantic import BaseModel, Field
from typing import List

class Category(BaseModel):

    category_name: str
    efforts: List = [Effort]

class Effort(BaseModel):
    author: str
    tasks: List = [Task]

class Task(BaseModel):
    author: str
    descr: str
    participants: List = [User]

class User(BaseModel):
    name: str
    
    """
    @validator('email')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
    """



