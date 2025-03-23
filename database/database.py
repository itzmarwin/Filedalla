#(©)CodeXBotz

import pymongo
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]  # "Anon" database connect hoga

# Old Mikasa bot ke users ko fetch karne ke liye collection name 'tgusersdb' set kiya
user_data = database['tgusersdb']  

async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    return [doc['_id'] async for doc in user_data.find()]

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
