from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.collection import Collection
from app.config import settings

client = None

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_DETAILS)

async def close_mongo_connection():
    client.close()

def get_user_collection() -> Collection:
    return client.app_db.users
