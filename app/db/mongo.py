
from pymongo.mongo_client import MongoClient
from app.core.settings import MONGO_CONNECTION_STRING, MONGO_DB_NAME

uri = f"{MONGO_CONNECTION_STRING}?appName={MONGO_DB_NAME}"
client = MongoClient(uri)

db = client[MONGO_DB_NAME]