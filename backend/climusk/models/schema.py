from pydantic import BaseModel, Field, validator, validate_arguments, ValidationError, EmailStr

from typing import List


class User(BaseModel):
    email: EmailStr
    points: int
    country: str
    following: List = [User]
    followers: List = [User]
    tasks: List = [Status]

    # required fields
    uuid: String = Field(...)
    name: str = Field(...)

    @validator('email')
    def email_must_contain_space(cls, v):
        if '@' not in v:
            raise ValueError('must contain a @')
        return v.title()

class Task(BaseModel):

    author_id: str = Field(...)
    descr: str
    points: int

class Status(BaseModel):

    task_id: str = Field(...)
    status: str = Field(...)

class Effort(BaseModel):

    author_id: str = Field(...)
    tasks: List[Task] = []
    participants: List[User] = []

class CategorySchema(BaseModel):

    category_name: str
    efforts: List[Effort] = []

class Feed(BaseModel):
    user_id: str
    messages: List[FeedMessage] = []

class FeedMessage(BaseModel):
    message: str
