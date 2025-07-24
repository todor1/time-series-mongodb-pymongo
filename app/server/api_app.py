from contextlib import asynccontextmanager

from fastapi import FastAPI
from server.models.database import init_db
from server.routes.device import router as device_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown (if needed)


api_app = FastAPI(lifespan=lifespan)

api_app.include_router(device_router, tags=["Device"])


@api_app.get("/", response_model=dict)
async def index():
    return {"message": "Welcome to the ECM Device Server API"}
