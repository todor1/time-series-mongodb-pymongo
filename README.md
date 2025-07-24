# Time Series with FastAPI and Beanie, or How to Handle Multiple Data Types and Not Go Crazy

**By Jorge B. Aspiazu**  
**Published: July 23, 2024**  
**Read time: 10 min**

**Original Article:** <https://medium.com/@jobenas_25464/time-series-with-fastapi-and-beanie-or-how-to-handle-multiple-data-types-and-not-go-crazy-05911237af5e>

---

**Author's note:** This is the second part of a series on IoT Cloud with MongoDB and other relevant technologies. For the first part of the series on how to set up MongoDB on a docker environment, you can go [here](https://medium.com/@jobenas_25464/deploying-mongodb-on-docker-for-iot-applications-d7ded714c5a3). For the version of this article in Spanish, you can go [here](https://medium.com/@jobenas_25464/gesti%C3%B3n-de-datos-de-sensores-iot-con-fastapi-y-beanie-c%C3%B3mo-manejar-m%C3%BAltiples-tipos-de-datos-sin-965ba8164a7b).

Managing different types of sensor data can be a real challenge, especially when using relational databases, which are the go-to choice for many cloud and web applications. However, MongoDB shines in this area because of its ability to store unstructured data. This flexibility allows us to store various types of data without the need to define table structures in advance.

When building a cloud solution, it's crucial that the database integrates smoothly with the web framework. Since I'm comfortable with Python, FastAPI is my preferred choice. Typically, in relational databases, we use an ORM like SQLAlchemy to interact with the database. For MongoDB, we need a similar tool to maintain flexibility and ease of use. This is where Beanie comes in.

In this post, I'll walk you through creating a simple HTTP RESTful API app that handles sensor data by inserting it into a MongoDB database and retrieving it as needed. Handling sensor data in a NoSQL database like MongoDB can be tricky since it's often time series data — data that's ordered in a sequence, usually by time. Our application will need to manage this effectively.

Before diving into the implementation, let's explore why we've chosen these specific technologies.

## Why FastAPI and Beanie?

Before diving into the implementation, let's discuss why we chose FastAPI and Beanie for this IoT cloud application.

### FastAPI

1. **Speed and Performance:** FastAPI is built on top of Starlette for the web parts and Pydantic for the data parts. It's designed to be fast and efficient, making it ideal for handling numerous concurrent requests typical in IoT applications.

2. **Ease of Use:** FastAPI's intuitive syntax and automatic generation of interactive API documentation (Swagger UI) make it very developer-friendly. This significantly speeds up the development process.

3. **Asynchronous Capabilities:** IoT applications often require handling real-time data. FastAPI's asynchronous capabilities allow it to handle many requests simultaneously, which is crucial for such applications.

### Beanie

1. **ODM for MongoDB:** Beanie simplifies interactions with MongoDB by providing an Object Document Mapper, similar to how an ORM works for SQL databases. This makes it easier to manage and query IoT data.

2. **Schema Validation:** Built on Pydantic, Beanie provides robust schema validation and data serialization. This ensures that the data being stored and retrieved is accurate and adheres to the defined schema.

3. **Integration with FastAPI:** Beanie integrates seamlessly with FastAPI, allowing for a cohesive and efficient development experience.

### MongoDB

1. **Flexible Schema:** IoT data can vary greatly in structure. MongoDB's flexible schema allows for efficient storage and retrieval of diverse data types without predefined schemas.

2. **Scalability:** MongoDB is designed to handle large volumes of data and can be scaled horizontally, making it suitable for IoT applications that generate a lot of data.

3. **Time Series Data:** MongoDB's time series collections provide optimizations for storing and querying time series data, which is ideal for IoT sensor data.

## Understanding Time Series Data and Its Challenges

### What is Time Series Data?

Time series data consists of data points indexed in time order. This type of data is crucial for tracking changes over time, making it essential for applications that monitor systems, performance, or other metrics. Examples include stock prices, weather data, and IoT sensor readings.

### Why IoT Sensor Data Fits into Time Series Data

IoT sensors continuously generate data points at regular intervals, creating a sequential flow of information. Each data point typically includes a timestamp and one or more readings (e.g., temperature, humidity). This temporal nature categorizes IoT sensor data as time series data. The need to store, query, and analyze this data efficiently is critical for extracting meaningful insights and responding to real-time events.

### Challenges of Handling Time Series Data in MongoDB

While MongoDB is versatile and excellent for unstructured data, managing time series data presents unique challenges:

1. **Volume and Velocity:** IoT sensors can generate vast amounts of data rapidly. MongoDB needs to handle high write loads efficiently.

2. **Query Performance:** Retrieving specific time ranges or aggregating data over time can be slower in MongoDB compared to specialized time series databases.

3. **Schema Flexibility:** Although MongoDB's flexible schema is beneficial, it can become cumbersome when dealing with highly structured time series data that requires precise indexing and querying.

### Benefits of Using MongoDB Over Specialized Time Series Databases

Despite these challenges, MongoDB offers several advantages for IoT applications over specialized time series databases like InfluxDB:

1. **Flexibility:** MongoDB's schema-less design allows for easy adjustments as the structure of the sensor data evolves.

2. **Unified Data Store:** MongoDB can store various types of data (not just time series) within the same database, providing a unified solution for applications requiring multiple data types.

3. **Robust Ecosystem:** MongoDB has a mature ecosystem with extensive tooling, libraries, and community support, making it easier to integrate with existing applications and services.

4. **Scalability:** MongoDB is designed for horizontal scalability, which is crucial for handling the increasing volume of IoT data.

5. **Aggregation Framework:** MongoDB's powerful aggregation framework allows for complex data processing and analysis within the database.

While specialized time series databases like InfluxDB are optimized for storing and querying time series data, MongoDB's flexibility, unified data storage capabilities, robust ecosystem, and scalability make it a strong candidate for IoT applications. These features allow developers to handle time series data efficiently while also managing other types of data within the same database.

In the next sections, we'll dive into how to set up FastAPI with Beanie to handle IoT sensor data, taking full advantage of MongoDB's capabilities to manage time series data effectively.

## Project and Prerequisites

This project will handle the creation of devices, as well as readings for these devices. Also the app will be able to retrieve individual devices, as well as list of them, while also being able to retrieve a list of sensor data that is restricted by timestamp range.

Before we dive in, make sure you have the following installed:

• Python 3.10+  
• FastAPI  
• MongoDB  
• Beanie  

### Project Structure

Here's a brief overview of our project structure:

```
app/
├── __init__.py
├── main.py
├── server/
│   ├── __init__.py
│   ├── api_app.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── device.py
│   ├── utils/
│       ├── pydantic_encoder.py
```

## Setting Up the Environment

Let's start by setting up our environment. Install the required packages using pip:

```bash
pip install fastapi beanie motor
```

## Connecting to MongoDB

First, we'll set up our MongoDB connection using Beanie. In `database.py`:

```python
from beanie import init_beanie
from motor import motor_asyncio
from app.server.models.models import Device, DeviceData

async def init_db():
    client = motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    database = client["ecm_mongo_db"]
    
    collection_names = await database.list_collection_names(filter={"name": "DeviceData"})
    if "device_data" not in collection_names:
        await database.command({
            "create": "DeviceData",
            "timeseries": {
                "timeField": "timestamp",
                "metaField": "metadata",
                "granularity": "seconds"
            }
        })
    
    await init_beanie(database=database, document_models=[Device, DeviceData])
```

If your database has a user/password authentication scheme you can adapt the AsyncIOMotorClient to the following:

```python
client = motor_asyncio.AsyncIOMotorClient("mongodb://<user>:<password>@localhost:27017")
```

It's important to notice that we're trying to create a time series collection that's called "DeviceData". Our objective with making the collection a time series is that, when querying the collection with timestamps, something that is extremely common in queries for sensor data, the search will be more efficient and faster.

## Defining Models and Schemas

Next, we'll define our data models using Beanie. In `models.py`:

```python
from pydantic import BaseModel, Field
from beanie import Document
from datetime import datetime

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
```

In this case we have defined a Device class that will act as our device definition, for each sensor we have we will have an entry on the Device collection. In this case we have defined a list of data types so we can have freedom of adding different types of sensors later on the life cycle of our application.

Also we have a DeviceData collection that we previously defined as a time series. In the definition of this class we add a metadata field, that we will use to identify the variable type being stored, this could come in handy if we want to search for all the data points containing a specific type of variable within a desired timestamp range.

We will also define a file called "schemas.py" which will contain the schema we will use to read the sensor data within our POST request route.

```python
from pydantic import BaseModel

class DeviceReading(BaseModel):
    value: dict[str, float]
    timestamp: int
```

This will come in handy later on, when we generate a standard way of sending data that can be used in the docs.

## Creating API Endpoints

We'll create endpoints to handle our IoT data in `device.py`:

```python
from datetime import datetime
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from starlette import status
from app.server.models.models import Device, DeviceData, ReadingMetadata
from app.server.models.schemas import DeviceReading

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
            detail=f"Device with ID {device_id} not found"
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
            detail=f"Device with ID {device_id} not found"
        )
    
    timestamp = datetime.fromtimestamp(reading.timestamp)
    value_keys = list(reading.value.keys())
    metadata = ReadingMetadata(
        variable_type=value_keys[0],
        device_id=str(device.id)
    )
    
    device_data = DeviceData(
        device_id=str(device_id),
        data=reading.value,
        timestamp=timestamp,
        metadata=metadata
    )
    
    await device_data.insert()
    return device_data

@router.get("/{device_id}/readings", response_model=list[DeviceData])
async def get_readings(
    device_id: PydanticObjectId,
    start_timestamp: int,
    end_timestamp: int
):
    device = await Device.get(device_id)
    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Device with ID {device_id} not found"
        )
    
    start_datetime = datetime.fromtimestamp(start_timestamp)
    end_datetime = datetime.fromtimestamp(end_timestamp)
    
    readings = await DeviceData.find(
        DeviceData.device_id == str(device_id),
        DeviceData.timestamp >= start_datetime,
        DeviceData.timestamp <= end_datetime
    ).to_list()
    
    return readings
```

Here we define specific routes to handle the different operations related to the device and the data. In a complete application, we might want to add a PUT request, as well as a DELETE request to the device, so we can update it, or delete entirely, the process in that regard is the same as what we're doing with the GET and POST requests.

An important observation here is that our `get_readings` endpoint uses integers as timestamps, which means we're receiving epoch values. This is a convenient way to handle the timestamps, so we can pass numbers without any tabulations or spaces on the query parameters in the URL. For testing purposes you can check the following [site](https://www.epochconverter.com/) that can give the epoch values for any timestamp.

## Integrating Routes in FastAPI

Finally, we'll integrate these routes into our FastAPI app in `api_app.py`:

```python
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
```

We add the router we declared on the "device.py" file, as well as the init_db function we created previously to handle the initialization of the database. We also add a route within this file to handle the root endpoint of our application.

## Running the Application

To run the application, create an `__init__.py` in the root directory to make the package importable and `main.py`:

```python
import uvicorn

if __name__ == "__main__":
    uvicorn.run("server.api_app:api_app", host="0.0.0.0", port=8080, reload=True)
```

This points to the api_app we created on the "api_app.py" file, by running the server like this is easier for us to test it just calling the python script on "main.py" like this.

```bash
python app/main.py
```

With this we can visit `http://localhost:8080/docs` to interact with the API. We should look to a view like the following.

Here we can test the different endpoints for inserting and retrieving the data. An important test is to check how the data points are retrieved when using the timestamps for range delimitation.

We can verify that the data is being stored correctly, with the metadata being stored as well. Is of particular note the fact that we can check the timestamps accordingly, and that all the timestamps belong to the specific range.

## Conclusion

In this blog post, we've walked through the process of setting up a FastAPI server with Beanie ODM to handle IoT sensor data as time series. This approach allows us to manage multiple data types effectively, leveraging MongoDB's flexibility while maintaining the performance and scalability required for real-time data processing.

By integrating FastAPI with Beanie, we created a powerful and efficient solution for handling complex data structures. FastAPI's speed, ease of use, and asynchronous capabilities make it an excellent choice for developing RESTful APIs, especially for IoT applications that require handling numerous concurrent requests. Beanie, with its seamless MongoDB integration, offers robust schema validation, easy querying, and data manipulation, making it easier to work with time series data.

## Key Takeaways

• **Flexibility:** MongoDB's schema-less nature allows for easy adaptation to evolving data structures, which is particularly beneficial for IoT applications where sensor data formats may change over time.

• **Unified Data Management:** Using MongoDB enables storing diverse data types in a single database, simplifying the architecture and reducing the complexity of managing multiple data stores.

• **Efficient Querying and Analysis:** Despite MongoDB not being a specialized time series database, its powerful aggregation framework and indexing capabilities make it suitable for efficient querying and analysis of time series data.

• **Scalability and Performance:** MongoDB's horizontal scalability ensures that your application can handle the increasing volume of IoT data, while FastAPI's asynchronous nature ensures high performance and responsiveness.

## Next Steps

Feel free to explore and extend this project to suit your specific needs. Whether you're adding more sophisticated data processing, implementing advanced querying features, or integrating with other services, the combination of FastAPI and Beanie provides a solid foundation for building scalable and efficient IoT applications.

Happy coding, and may your journey into IoT and time series data management be as smooth and exciting as possible!

---

**Tags:** Python, IoT, Database, MongoDB, FastAPI

**About the Author:** Jorge B. Aspiazu is an Electrical Engineer with a passion for technology, especially for programming languages.

## Git Workflow: Upload to New Branch  


Here's the complete workflow for creating and uploading changes to a new branch:

### 1. Check Current Branch
```bash
git branch --show-current
git branch -v
```

### 2. Create and Switch to New Branch
```bash
git checkout -b 'blog-post'
```

### 3. Stage All Changes
```bash
git add .
```

### 4. Commit Changes with Message
```bash
git commit -m "medium beanie start"
```

### 5. Push to Remote and Set Upstream
```bash
git push -u origin medium-beanie
```