from pymongo import MongoClient

connection_string = "mongodb+srv://testuser:DVcZ311ILLuJVTNQ@testcluster.2ud7h6w.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db_connection = client["csgTest"]
collection = db_connection.get_collection("github_users")

def save(data):
    collection.insert_one(data)
    
def update(filter, data):
    collection.update_one(filter, data)
    
def find_all_user_name():
    return collection.find({}, {"user_name": 1})

def find_all():
    return collection.find()
    