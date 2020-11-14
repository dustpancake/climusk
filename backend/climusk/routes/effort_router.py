from fastapi import APIRouter

from climusk.database import database
from climusk.models.schema import Effort


router = APIRouter()

effort_collection = database.get_collection("efforts")

async def retrieve_effort(effort_id):
    ret = await effort_collection.find_one({"effort_id":effort_id})
    return Effort(**ret)


@router.get("/{oid}")
async def get_effort(oid: str):
    return await retrieve_effort(oid)
