from pymongo.mongo_client import MongoClient
client = MongoClient("mongodb+srv://fastapi:BmUbMica2YZQmDag@cluster0.jnnz3ye.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.todo_db
collection_name = db["todo_collection"]
 