from beanie import init_beanie
from motor import motor_asyncio

from app.server.models.models import Device, DeviceData


async def init_db():
    client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
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
