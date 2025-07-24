from fastapi import FastAPI

from app.server.models.database import init_db
from app.server.routes.device import router as device_router

api_app = FastAPI()

api_app.include_router(device_router, tags=["Device"])


@api_app.on_event("startup")
async def start_db():
    await init_db()


@api_app.get("/", response_model=dict)
async def index():
    return {"message": "Welcome to the ECM Device Server API"}
