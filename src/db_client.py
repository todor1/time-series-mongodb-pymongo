# blank on purpose - check `final` branch
from functools import lru_cache
from pymongo import MongoClient
from decouple import config


@lru_cache
def get_db_client():
    mongodb_un = config("MONGO_INITDB_ROOT_USERNAME")
    mongodb_pw = config("MONGO_INITDB_ROOT_PASSWORD")
    mongodb_host = config("MONGO_HOST", default="localhost")
    # ports from docker-compose.yaml file
    db_url = f"mongodb://{mongodb_un}:{mongodb_pw}@{mongodb_host}:27017"
    return MongoClient(db_url)
