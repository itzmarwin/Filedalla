#(©)CodeXBotz

from motor.motor_asyncio import AsyncIOMotorClient
from config import DB_URI, DB_NAME

client = AsyncIOMotorClient(DB_URI)
database = client[DB_NAME]

# Use same collection name as music bot
user_data = database.tgusersdb  # Changed from 'users' to 'tgusersdb'

async def present_user(user_id: int):
    user = await user_data.find_one({"user_id": user_id})  # Changed _id to user_id
    return bool(user)

async def add_user(user_id: int):
    await user_data.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def full_userbase():
    return [doc["user_id"] async for doc in user_data.find({"user_id": {"$gt": 0}}, {"user_id": 1})]  # Music bot style query

async def del_user(user_id: int):
    await user_data.delete_one({"user_id": user_id})
