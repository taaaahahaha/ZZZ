import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://taaham:123@cluster0.imuxc.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["Todo"]
collection = db["Data"]

collection.insert_one({
    "title":"Titlew",
    "desc":"Desc2"
    })