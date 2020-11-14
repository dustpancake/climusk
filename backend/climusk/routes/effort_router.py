from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Effort, Task


router = APIRouter()

effort_collection = database.get_collection("efforts")

async def retrieve_effort(effort_id):
    ret = await effort_collection.find_one({"effort_id":effort_id})
    return Effort(**ret)


@router.get("/{oid}")
async def get_effort(oid: str):
    return await retrieve_effort(oid)

@router.post("/")
async def insert_task(task: Task):
  ret = await task_collection.insert_one(task.dict(exclude_unset=True))
  ##print(ret.inserted_id)
  return {"id": str(ret.inserted_id)}

async def add_task_to_effort(task, effort):

    cat = await effort_collection.find_one(
        {"effort_name": effort}
    ) 
    if not cat:
        return JSONResponse(status_code=400, content={"message": "bad category"})

    updated_tasks = cat.get("tasks", [])
    updated_tasks.append(task.dict(exclude_unset=True))
    resp = await effort_collection.update_one(
        {"effort_name": effort}, {"$set": {"tasks": updated_tasks}}
    )
    return {"modified": resp.modified_count, "message": "ok"}

# add effort to category
@router.post("/{effort}")
async def add_task(effort: str, task: Task):
    return await add_task_to_effort(task, effort)