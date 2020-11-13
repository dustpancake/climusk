from pydantic import BaseModel, Field
from typing import List

class CategorySchema(BaseModel):

    category_name: str = Field(...)
    efforts: List = []
