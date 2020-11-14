from pydantic import BaseModel, Field, validator, validate_arguments, ValidationError, EmailStr

from typing import List

class Status(BaseModel):

    # required fields
    task_id: str = Field(...)
    status: str = Field(...)

class User(BaseModel):
    email: EmailStr = None
    points: int = None
    country: str = None
    following: List[str] = []
    followers: List[str] = []
    tasks: List[Status] = []

    # required fields
    uuid: str = Field(...)
    name: str = Field(...)

    @validator('email')
    def email_must_contain_space(cls, v):
        if '@' not in v:
            raise ValueError('must contain a @')
        return v.title()

class Task(BaseModel):

    # required fields
    author_id: str = Field(...)

    name: str = None
    descr: str = None
    points: int = None

class Effort(BaseModel):

    # required fields
    author_id: str = Field(...)
    name: str = Field(...)

    tasks: List[Task] = None
    participants: List[User] = None

class CategorySchema(BaseModel):

    category_name: str = None
    efforts: List[Effort] = []

class FeedMessage(BaseModel):
    message: str = None

class Feed(BaseModel):
    user_id: str = None
    messages: List[FeedMessage] = []
