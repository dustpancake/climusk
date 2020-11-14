from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Task, User, Effort


router = APIRouter()

task_collection = database.get_collection("tasks")
effort_collection = database.get_collection("efforts")


async def retrieve_task(task_id):
  ret = await task_collection.find_one({"task_id":task_id})
  return Task(**ret)

@router.post("/")
async def insert_task(task: Task):
  ret = await task_collection.insert_one(task.dict(exclude_unset=True))
  ##print(ret.inserted_id)
  return {"id": str(ret.inserted_id)}

@router.post("/{effort_oid}")
async def add_task_to_effort(effort_oid: str, task: Task):
  ret = await effort_collection.insert_one(task.dict(exclude_unset=True))


@router.get("/{oid}")
async def get_task(oid: str):
    return await retrieve_task(oid)





