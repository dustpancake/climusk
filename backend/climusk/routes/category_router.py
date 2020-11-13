from fastapi import APIRouter

from climusk.database import database
from climusk.models.category import CategorySchema, Task


router = APIRouter()

category_collection = database.get_collection("categories")

async def retrieve_categories():
    ret = []
    async for cat in category_collection.find():
        ret.append(CategorySchema(**cat))
    return ret


@router.get("/{name}")
async def get_category(name: str):
    return await retrieve_categories()


@router.post("/task")
async def post_task(task: Task):
    print(type(task))
    print(task)
    return {}
