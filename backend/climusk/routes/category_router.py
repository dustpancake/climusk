from fastapi import APIRouter

router = APIRouter()

@router.get("/{name}")
async def get_category(name: str):
    return {"message":name}
