from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Task


router = APIRouter()

task_collection = database.get_collection("tasks")

async def retrieve_task(task_id):
  ret = await task_collection.find_one({"task_id":task_id})
  return Task(**ret)

@router.get("/{oid}")
async def get_task(oid: str):
    return await retrieve_task(oid)





