from beanie import init_beanie
from decouple import config
from motor import motor_asyncio

from app.server.models.models import Device, DeviceData


async def init_db():
    # client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    # in case of authenticaion use below:
    mongodb_un = config("MONGO_INITDB_ROOT_USERNAME")
    mongodb_pw = config("MONGO_INITDB_ROOT_PASSWORD")
    mongodb_host = config("MONGO_HOST", default="localhost")
    # ports from docker-compose.yaml file
    db_url = f"mongodb://{mongodb_un}:{mongodb_pw}@{mongodb_host}:27017"
    client = motor_asyncio.AsyncIOMotorClient(db_url)
    database = client["ecm_mongo_db"]

    collection_names = await database.list_collection_names(
        filter={"name": "DeviceData"}
    )
    if "device_data" not in collection_names:
        await database.command(
            {
                "create": "DeviceData",
                "timeseries": {
                    "timeField": "timestamp",
                    "metaField": "metadata",
                    "granularity": "seconds",
                },
            }
        )

    await init_beanie(database=database, document_models=[Device, DeviceData])
