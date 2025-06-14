import os
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus

# Load credentials from .env
load_dotenv()

username = quote_plus(os.getenv("MONGO_USER"))         # safely encode username
password = quote_plus(os.getenv("MONGO_PASSWORD"))     # safely encode password
cluster_url = os.getenv("MONGO_CLUSTER_URL")           # e.g., cluster0.az5ego2.mongodb.net
database_name = os.getenv("MONGO_DB_NAME")             # e.g., spotifyDB

# Construct safe MongoDB URI
MONGO_URI = f"mongodb+srv://{username}:{password}@{cluster_url}/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB_NAME = database_name

# Return collection connection
def get_mongo_collection(collection_name):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB_NAME]
    return db[collection_name]
