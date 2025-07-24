from pydantic import BaseModel


class DeviceReading(BaseModel):
    value: dict[str, float]
    timestamp: int
