from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import User


router = APIRouter()

user_collection = database.get_collection("users")

async def retrieve_users(query):
  ret = await user_collection.find_one(query)
  return User(**ret)

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
