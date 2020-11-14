from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Task, User, Effort


router = APIRouter()

task_collection = database.get_collection("tasks")

async def retrieve_effort(effort_id):
  ret = await effort_collection.find_one({"effort_id":effort_id})
  return Effort(**ret)

@router.post("/{effort_oid}")
async def add_task_to_effort(effort_oid, task):
  ret = await user_collection.insert_one(user.dict(exclude_unset=True))
  print(ret.inserted_id)
  return {"id": str(ret.inserted_id)}

@router.get("/{oid}")
async def get_effort(oid: str):
    return await retrieve_effort(oid)





