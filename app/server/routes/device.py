from datetime import datetime

from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from server.models.models import Device, DeviceData, ReadingMetadata
from server.models.schemas import DeviceReading
from starlette import status

router = APIRouter(prefix="/device", tags=["Device"])


@router.get("/")
async def get_devices():
    devices = await Device.all().to_list()
    return devices


@router.get("/{device_id}")
async def get_device(device_id: PydanticObjectId):
    device = await Device.get(device_id)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device with ID {device_id} not found",
        )
    return device


@router.post("/")
async def create_device(device: Device):
    await device.insert()
    return device


@router.post("/{device_id}/reading", response_model=DeviceData)
async def add_reading(device_id: PydanticObjectId, reading: DeviceReading):
    device = await Device.get(device_id)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device with ID {device_id} not found",
        )

    timestamp = datetime.fromtimestamp(reading.timestamp)
    value_keys = list(reading.value.keys())
    metadata = ReadingMetadata(variable_type=value_keys[0], device_id=str(device.id))

    device_data = DeviceData(
        device_id=str(device_id),
        data=reading.value,
        timestamp=timestamp,
        metadata=metadata,
    )

    await device_data.insert()
    return device_data


@router.get("/{device_id}/readings", response_model=list[DeviceData])
async def get_readings(
    device_id: PydanticObjectId, start_timestamp: int, end_timestamp: int
):
    device = await Device.get(device_id)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device with ID {device_id} not found",
        )

    start_datetime = datetime.fromtimestamp(start_timestamp)
    end_datetime = datetime.fromtimestamp(end_timestamp)

    readings = await DeviceData.find(
        DeviceData.device_id == str(device_id),
        DeviceData.timestamp >= start_datetime,
        DeviceData.timestamp <= end_datetime,
    ).to_list()

    return readings
