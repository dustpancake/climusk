from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Effort, Task


router = APIRouter()

effort_collection = database.get_collection("efforts")
task_collection = database.get_collection("tasks")

async def retrieve_effort(effort_id):
    ret = await effort_collection.find_one({"effort_id":effort_id})
    return Effort(**ret)

async def add_task_to_effort(task, effort):
    eff = await effort_collection.find_one(
        {"effort_name": effort}
    ) 
    if not eff:
        return JSONResponse(status_code=400, content={"message": "bad effort"})
    
    ret = await task_collection.insert_one(task.dict(exclude_unset=True))

    updated_tasks = eff.get("tasks", [])
    updated_tasks.append(task.dict(exclude_unset=True))
    resp = await effort_collection.update_one(
        {"effort_name": effort}, {"$set": {"tasks": updated_tasks}}
    )
    return {"id": str(ret.inserted_id), "modified": resp.modified_count, "message": "ok"}

@router.get("/{oid}")
async def get_effort(oid: str):
    return await retrieve_effort(oid)

# add task to effort
@router.post("/{effort}")
async def add_task(effort: str, task: Task):
    return await add_task_to_effort(task, effort)