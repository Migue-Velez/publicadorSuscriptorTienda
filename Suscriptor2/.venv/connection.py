import pymongo

def sendMessage(message):
    client = pymongo.MongoClient("localhost:27017")
    db = client["suscriptor1"]
    collection = db["messages"]
    collection.insert_one(message)