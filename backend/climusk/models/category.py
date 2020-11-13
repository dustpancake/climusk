from pydantic import BaseModel, Field
from typing import List

class Task(BaseModel):

    author: str
    descr: str

class Effort(BaseModel):

    author: str
    tasks: List = [Task]
    participants: List = []

class CategorySchema(BaseModel):

    category_name: str
    efforts: List[Effort] = []


class User(BaseModel):
    name: str

    """
    @validator('email')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()
    """
