from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import CategorySchema, Task


router = APIRouter()

efforts_collection = database.get_collection("efforts")

async def efforts_collection():
    
    return efforts_collection.find_one()


class Effort(BaseModel):

    author_id: str = Field(...)
    tasks: List[Task] = []
    participants: List[User] =

@router.get("/{name}")
async def get_category(name: str):
    return await retrieve_categories({"name":name})


@router.post("/task")
async def post_task(task: Task):
    print(type(task))
    print(task)
    return {}
