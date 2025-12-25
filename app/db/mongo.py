
from pymongo.mongo_client import MongoClient
from app.core.settings import MONGO_CONNECTION_STRING, MONGO_DB_NAME

uri = f"{MONGO_CONNECTION_STRING}?appName={MONGO_DB_NAME}"
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)