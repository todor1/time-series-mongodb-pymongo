from datetime import datetime

from beanie import Document
from pydantic import BaseModel, Field


class Device(Document):
    name: str = Field(...)
    location: dict[str, float] = Field(...)
    data_types: list[str] = Field(...)

    class Settings:
        collection = "Device"


class ReadingMetadata(BaseModel):
    variable_type: str
    device_id: str


class DeviceData(Document):
    device_id: str = Field(...)
    data: dict[str, float] = Field(...)
    timestamp: datetime = Field(...)
    metadata: ReadingMetadata = Field(...)

    class Settings:
        collection = "DeviceData"
