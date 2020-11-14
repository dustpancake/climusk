from fastapi import APIRouter
from fastapi.responses import JSONResponse

from climusk.database import database
from climusk.models.schema import CategorySchema, Task, Effort


router = APIRouter()

category_collection = database.get_collection("categories")


async def retrieve_categories():
    ret = []
    async for cat in category_collection.find():
        ret.append(CategorySchema(**cat))
    return ret


async def add_effort_to_category(effort, category):
    # validation taken care of by fastapi
    cat = await category_collection.find_one(
        {"category_name": category}
    )  #  get current value
    if not cat:
        return JSONResponse(status_code=400, content={"message": "bad category"})

    updated_efforts = cat.get("efforts", [])
    updated_efforts.append(effort.dict(exclude_unset=True))
    resp = await category_collection.update_one(
        {"category_name": category}, {"$set": {"efforts": updated_efforts}}
    )
    return {"modified": resp.modified_count, "message": "ok"}


# add effort to category
@router.post("/{category}")
async def add_effort(category: str, effort: Effort):
    return await add_effort_to_category(effort, category)


@router.get("/")
async def get_category():
    return await retrieve_categories()


@router.post("/task")
async def post_task(task: Task):
    print(type(task))
    print(task)
    return {}
