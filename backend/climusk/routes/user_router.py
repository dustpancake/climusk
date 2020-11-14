from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import User


router = APIRouter()

user_collection = database.get_collection("users")
effort_collection = database.get_collection("efforts")


async def retrieve_users(query):
  ret = await user_collection.find_one(query)
  return User(**ret)

async def add_user_to_effort(user, effort):
    eff = await effort_collection.find_one(
        {"effort_name": effort}
    ) 
    if not eff:
        return JSONResponse(status_code=400, content={"message": "bad effort"})
    
    ret = await user_collection.find_one(user)

    updated_user = eff.get("users", [])
    updated_user.append(user.dict(exclude_unset=True))
    resp = await effort_collection.update_one(
        {"effort_name": effort}, {"$set": {"user": updated_user}}
    )
    return {"id": str(ret.inserted_id), "modified": resp.modified_count, "message": "ok"}

@router.get("/name/{name}")
async def get_user(name: str):
    return await retrieve_users({"name":name})

@router.get("/id/{_id}")
async def get_user(_id: str):
    return await retrieve_users({"id":_id})

@router.post("/")
async def post_user(user: User):
  ret = await user_collection.insert_one(user.dict(exclude_unset=True))
  print(ret.inserted_id)
  return {"id": str(ret.inserted_id)}

# add user to effort
@router.post("/{effort}")
async def add_user(effort: str, user: User):
    return await add_user_to_effort(user, effort)
