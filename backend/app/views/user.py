from fastapi import APIRouter, HTTPException, Depends
from pymongo.collection import Collection
from app.database import get_user_collection
from app.models.user import User
from app.schemas.user import UserCreate

router = APIRouter()

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate, users: Collection = Depends(get_user_collection)):
    user_dict = user.dict()
    result = await users.insert_one(user_dict)
    user_dict["_id"] = result.inserted_id
    return user_dict
