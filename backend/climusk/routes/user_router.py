from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import User


router = APIRouter()

user_collection = database.get_collection("users")

async def retrieve_users(name):
  ret = await user_collection.find_one({"name":name})
  return User(**ret)

@router.get("/{name}")
async def get_user(name: str):
    return await retrieve_users()

@router.post("/user")
async def post_user(user: User):
  ret = await user_collection.insert_one(user.dict(exclude_unset=True))
  print(ret.inserted_id)
  return {"id": str(ret.inserted_id)}
