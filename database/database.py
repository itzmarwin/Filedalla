#(©)CodeXBotz

import pymongo
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]
user_data = database['tgusersdb']

async def present_user(user_id: int):
    return bool(user_data.find_one({'_id': user_id}))

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})

async def full_userbase():
    # Async for की जगह synchronous loop use करें
    return [doc['_id'] for doc in user_data.find({}, {'_id': 1})]

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
