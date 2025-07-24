# FastAPI Beanie IoT Application

This is a FastAPI application with Beanie ODM for handling IoT sensor data with MongoDB time series collections.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt

source .venv/Scripts/activate
uv add -r app/requirements.txt
```

2. Make sure MongoDB is running on localhost:27017

3. Run the application:
```bash
python main.py
```

4. Visit http://localhost:8080/docs for the interactive API documentation

## Project Structure

- `main.py` - Application entry point
- `server/api_app.py` - FastAPI application setup
- `server/models/` - Data models and database connection
- `server/routes/` - API endpoints
- `server/utils/` - Utility functions

---

# Deploying MongoDB on Docker for IoT Applications

**By Jorge B. Aspiazu**  
**Published: June 4, 2024**  
**Read time: 15 min**

**Original Article:** <https://medium.com/@jobenas_25464/deploying-mongodb-on-docker-for-iot-applications-d7ded714c5a3>

**Note:** The Spanish version of this article is available [here](https://medium.com/@jobenas_25464/desplegando-mongodb-en-docker-para-aplicaciones-de-iot-68ef55d4a3df).

## Introduction to MongoDB and Docker

Among databases, MongoDB is one of the most prominent NoSQL databases currently, is like the Swiss Army knife of databases — it's versatile, scalable, and adept at handling unstructured data. Meanwhile, Docker, the best known technology for containerization, is revolutionizing the way we deploy and manage applications. These two technologies combined provide ample benefits that allow for very simple, scalable and reproducible deployments that allow for ease of use and allow better tools for development as well.

This is especially true in the realm of Internet of Things (IoT) development, where data comes in all shapes and sizes, having a flexible and efficient database solution is paramount. MongoDB fits the bill perfectly, offering a schema-less design that adapts seamlessly to the ever-changing data landscape of IoT devices. In a scenario where different types of sensors generate data in different formats, a flexible data repository with incredible performance like MongoDB is an incredibly powerful solution.

As powerful as MongoDB is, deploying a database is always a cumbersome proposition, especially with all the configuration needed, this is doubly true for any development environment, where it might be necessary to run an instance of the database that should mimic exactly what the production environment might be. For this type of scenario Docker swoops in to simplify the deployment process, allowing you to spin up MongoDB instances with just a few commands, whether you're on your local laptop or scaling up in the cloud. With Docker, gone are the days of wrestling with dependency hell and configuration nightmares — say hello to consistency and portability across different environments.

So in this article we will explore how to combine these two powerful tools to make development of IoT applications a really easy and enjoyable experience.

## Advantages of Using Docker for MongoDB

Deploying MongoDB using Docker isn't just convenient; it's a game-changer for developers and IT professionals alike. Here's why:

1. **Portability:** One of Docker's standout features is its ability to ensure your MongoDB environment runs seamlessly across different machines and platforms. Whether you're on a Windows laptop, a macOS desktop, or a Linux server, Docker ensures that your MongoDB container behaves consistently. This eliminates the classic "works on my machine" problem, making collaboration and deployment a breeze.

2. **Scalability:** With Docker, scaling your MongoDB deployment is as easy as scaling up your favorite recipe. Need more capacity? Simply spin up additional containers. Docker's orchestration tools, like Docker Swarm or Kubernetes, further simplify scaling by managing the deployment of multiple containers across a cluster of machines, ensuring that your database can grow alongside your application.

3. **Ease of Setup:** Setting up MongoDB in a traditional environment can involve a labyrinth of configurations and dependencies. Docker cuts through this complexity with straightforward commands that can pull the MongoDB image and run it within minutes. This ease of setup accelerates the development process, allowing you to focus on building features rather than managing infrastructure.

4. **Isolation:** Docker containers provide an isolated environment for your MongoDB instance. This isolation means that different applications and services can run on the same machine without interfering with each other. Each container has its own resources and dependencies, ensuring that changes or issues in one container do not impact others.

5. **Consistency:** By encapsulating MongoDB and its environment within a Docker container, you achieve consistency across development, testing, and production environments. This means fewer surprises and bugs when transitioning your application through different stages of the development lifecycle.

Docker makes deploying MongoDB locally not just easy, but also highly efficient and scalable. It's like having a personal assistant that ensures everything runs smoothly, regardless of where you are or what you're working on.

## Setting Up Docker

Before we can deploy MongoDB using Docker, we need to ensure Docker is installed on your local laptop. Here's how to get Docker up and running on different operating systems.

### Windows

**Download Docker Desktop:**
• Visit the [Docker Desktop for Windows page](https://docs.docker.com/desktop/install/windows-install/).
• Click on "Docker Desktop for Windows."

**Install Docker Desktop:**
• Run the downloaded installer.
• Follow the on-screen instructions to complete the installation.
• During installation, ensure the option "Use the WSL 2 based engine" is checked for better performance.

**Start Docker Desktop:**
• Launch Docker Desktop from the Start menu.
• Wait for Docker to start; you'll see the Docker icon in the system tray once it's running.

### macOS

**Download Docker Desktop:**
• Visit the [Docker Desktop for Mac page](https://docs.docker.com/desktop/install/mac-install/).
• Click on the option that is suitable for your type of computer.

**Install Docker Desktop:**
• Open the downloaded `.dmg` file.
• Drag the Docker icon to the Applications folder.

**Start Docker Desktop:**
• Open Docker from the Applications folder.
• Follow any prompts to complete the installation.
• Wait for Docker to start; you'll see the Docker icon in the menu bar once it's running.

### Linux

**Update Your Package Index:**
```bash
sudo apt-get update
```

**Install Required Packages:**
```bash
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

**Add Docker's Official GPG Key:**
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

**Set Up the Stable Repository:**
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

**Install Docker Engine:**
```bash
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

**Start Docker:**
```bash
sudo systemctl start docker
```

**Enable Docker to Start at Boot:**
```bash
sudo systemctl enable docker
```

### Verify Docker Installation

After installing Docker, verify that it's installed correctly by running the following command in your terminal or command prompt:

```bash
docker --version
```

You should see the Docker version information displayed. Now, you're ready to deploy MongoDB using Docker!

## Pulling MongoDB Docker Image

Now that Docker is up and running on your machine, it's time to pull the official MongoDB Docker image from Docker Hub. This image contains everything you need to run MongoDB within a Docker container.

### Steps to Pull MongoDB Docker Image

**Open Your Terminal or Command Prompt:**
• On Windows, you can use Command Prompt, PowerShell, or any other terminal emulator.
• On macOS and Linux, you can use the default terminal application.

**Log In to Docker Hub (Optional):**
• If you have a Docker Hub account, you can log in to avoid rate limits and access private images if needed.
```bash
docker login
```

**Pull the Official MongoDB Image:**
• Use the following command to pull the latest MongoDB image from Docker Hub.
```bash
docker pull mongo
```
• If you want to pull a specific version of MongoDB, you can specify the version tag. For example, to pull version 4.4:
```bash
docker pull mongo:4.4
```

**Verify the Downloaded Image:**
• List the Docker images on your system to verify that the MongoDB image has been pulled successfully.
```bash
docker images
```
• You should see an entry for mongo in the output list.

By following these steps, you now have the MongoDB Docker image on your local machine, ready to be used for creating and running MongoDB containers.

## Running MongoDB Container

Once you've pulled the MongoDB image from Docker Hub, the next step is to create and run a MongoDB container. It's important to understand the difference between pulling an image and running a container: pulling an image downloads the application package, while running a container creates an isolated environment where the application runs.

### Steps to Run a MongoDB Container

**Open Your Terminal or Command Prompt:**
• On Windows, use Command Prompt, PowerShell, or any other terminal emulator.
• On macOS and Linux, use the default terminal application.

**Run the MongoDB Container:**
• Use the following command to run a MongoDB container:
```bash
docker run --name mongodb-container -d -p 27017:27017 -v mongodata:/data/db -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

Let's break down what each option in the command means:
• `docker run`: The command to create and start a new container.
• `--name mongodb-container`: Names the container "mongodb-container" for easier identification.
• `-d`: Runs the container in detached mode (in the background).
• `-p 27017:27017`: Maps port 27017 of the host to port 27017 of the container. This allows you to access MongoDB from your local machine.
• `-v mongodata:/data/db`: Creates a Docker volume named "mongodata" and mounts it to the `/data/db` directory in the container. Volumes are used to persist data outside of the container's lifecycle.
• `-e MONGO_INITDB_ROOT_USERNAME=admin`: Sets the environment variable `MONGO_INITDB_ROOT_USERNAME` to "admin". This initializes the MongoDB root username.
• `-e MONGO_INITDB_ROOT_PASSWORD=password`: Sets the environment variable `MONGO_INITDB_ROOT_PASSWORD` to "password". This initializes the MongoDB root password.
• `mongo`: Specifies the Docker image to use, in this case, the official MongoDB image.

**Verify the Container is Running:**
• List the running Docker containers to verify that your MongoDB container is up and running.
```bash
docker ps
```
• You should see mongodb-container listed with the status "Up".

By following these steps, you now have a running MongoDB container that you can use to develop your IoT applications. This container runs in isolation, providing a consistent and portable environment for your MongoDB instance.

## Accessing MongoDB Container

Now that your MongoDB container is up and running, you'll want to access the MongoDB database to start managing your data. You can do this using the MongoDB shell (`mongosh`) or a MongoDB client. Let's explore both methods.

### Using the MongoDB Shell

The MongoDB shell is an interactive JavaScript interface for MongoDB, allowing you to run queries and perform administrative tasks.

**Access the MongoDB Shell Inside the Container:**
• Use the following command to start an interactive terminal session inside the running MongoDB container:
```bash
docker exec -it mongodb-container mongosh -u admin -p password
```
• Let's break down the command:
  • `docker exec -it`: Runs a command in a running container with interactive terminal mode.
  • `mongodb-container`: The name of the container where MongoDB is running.
  • `mongosh -u admin -p password`: Launches the MongoDB shell inside the container, using the `admin` username and `password` password you set earlier. It is important to note that on latest images the command is mongosh, in earlier versions it was mongo.

**Interact with MongoDB:**
• Once inside the MongoDB shell, you can run commands to interact with the database. For example, to show all databases:
```javascript
show dbs
```

To switch to a specific database:
```javascript
use mydatabase
```

To display all collections in the current database:
```javascript
show collections
```

### Using a MongoDB Client

A MongoDB client provides a graphical user interface to interact with your MongoDB database, making it easier for those who prefer not to use the command line.

**Download and Install a MongoDB Client:**
• Popular MongoDB clients include [MongoDB Compass](https://www.mongodb.com/products/compass) and [Robo 3T](https://robomongo.org/).

**Connect to the MongoDB Container:**
• Open your MongoDB client and create a new connection.
• Use the following connection settings:
  • Hostname: `localhost`
  • Port: `27017`
  • Authentication:
    • Database: `admin`
    • Username: `admin`
    • Password: `password`

**Manage Your Database:**
• Once connected, you can use the client to browse databases, create collections, insert documents, and perform other administrative tasks through an intuitive GUI.

By following these steps, you can easily access and manage your MongoDB database running inside the Docker container, either through the MongoDB shell or a client.

## Data Persistence

In containerized environments, ensuring data persistence is crucial because containers are ephemeral by nature. When a container is stopped or removed, any data stored inside the container is lost. This is where Docker volumes come into play, providing a way to persist data beyond the lifecycle of individual containers.

### Understanding Docker Volumes

A Docker volume is a storage location outside of the container's file system that can be mounted into one or more containers. Volumes are managed by Docker and can be used to store data that needs to persist across container restarts and even across different containers.

### Why Data Persistence Matters

For applications like MongoDB, which stores critical data, it's essential to ensure that the data is not lost when the container is restarted or updated. By using Docker volumes, we can:

• **Maintain Data Integrity:** Ensure that data remains consistent and intact regardless of container restarts.
• **Facilitate Backups:** Simplify the process of backing up and restoring data.
• **Enable Data Sharing:** Share data between multiple containers easily.

### Configuring Docker Volumes for MongoDB

To demonstrate how to configure Docker volumes for MongoDB, we'll modify our Docker run command to include volume settings that persist MongoDB data.

**Create and Run a MongoDB Container with a Volume:**
• Use the following command to run a MongoDB container with a volume:
```bash
docker run --name mongodb-container -d -p 27017:27017 -v mongodata:/data/db -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```

Let's break down the volume part of this command:
• `-v mongodata:/data/db`: This creates a Docker volume named "mongodata" and mounts it to the `/data/db` directory inside the container. The `/data/db` directory is where MongoDB stores its data files.

**Verify the Volume:**
• List Docker volumes to ensure the volume "mongodata" has been created:
```bash
docker volume ls
```

**Inspect the Volume:**
• To inspect the details of the volume, use:
```bash
docker volume inspect mongodata
```

**Persisting Data Across Container Restarts:**
• Stop and remove the MongoDB container:
```bash
docker stop mongodb-container
docker rm mongodb-container
```
• Run a new MongoDB container using the same volume:
```bash
docker run --name mongodb-container -d -p 27017:27017 -v mongodata:/data/db -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=password mongo
```
• The data in the "mongodata" volume will persist across container restarts and removals, ensuring your data remains intact.

By configuring Docker volumes, we ensure that our MongoDB data is safely stored and persists beyond the lifecycle of any single container, providing stability and reliability for your IoT applications.

## Basic MongoDB Operations

Now that your MongoDB container is running and data persistence is configured, let's dive into some basic MongoDB operations. Understanding these key operations is essential for effectively managing your database. We'll cover creating databases and collections, inserting documents, querying data, and updating documents.

### Creating Databases and Collections

In MongoDB, databases hold collections, and collections hold documents. Documents are the basic units of data in MongoDB, similar to rows in a relational database.

**Creating a Database:**
• MongoDB creates a new database implicitly when you switch to a non-existent database and insert data. Use the `use` command to switch to a new database.
```javascript
use mydatabase
```

**Creating a Collection:**
• Collections are created when you insert the first document into them. To create a collection explicitly:
```javascript
db.createCollection("mycollection")
```

### Inserting Documents

Documents in MongoDB are stored in JSON-like format called BSON (Binary JSON).

**Inserting a Single Document:**
• Use the `insertOne` method to insert a single document into a collection.
```javascript
db.mycollection.insertOne({ name: "John Doe", age: 30, occupation: "Engineer" })
```

**Inserting Multiple Documents:**
• Use the `insertMany` method to insert multiple documents at once.
```javascript
db.mycollection.insertMany([
   { name: "Jane Smith", age: 25, occupation: "Designer" },
   { name: "Sam Brown", age: 40, occupation: "Manager" }
])
```

### Querying Data

Querying in MongoDB is flexible and allows for a variety of filtering criteria.

**Finding All Documents:**
• Use the `find` method to retrieve all documents in a collection.
```javascript
db.mycollection.find()
```

**Finding Documents with a Filter:**
• Use the `find` method with a filter to retrieve documents that match specific criteria.
```javascript
db.mycollection.find({ age: { $gt: 30 } })
```

**Finding a Single Document:**
• Use the `findOne` method to retrieve a single document that matches the criteria.
```javascript
db.mycollection.findOne({ name: "John Doe" })
```

### Updating Documents

Updating documents in MongoDB can be done using several methods, depending on the requirement.

**Updating a Single Document:**
• Use the `updateOne` method to update a single document that matches the filter.
```javascript
db.mycollection.updateOne(
   { name: "John Doe" },
   { $set: { age: 31 } }
)
```

**Updating Multiple Documents:**
• Use the `updateMany` method to update multiple documents that match the filter.
```javascript
db.mycollection.updateMany(
   { occupation: "Engineer" },
   { $set: { department: "Technology" } }
)
```

**Replacing a Document:**
• Use the `replaceOne` method to replace an entire document.
```javascript
db.mycollection.replaceOne(
   { name: "John Doe" },
   { name: "John Doe", age: 31, occupation: "Senior Engineer"}
)
```

These basic operations form the foundation of working with MongoDB. Mastering them will enable you to efficiently manage your database and handle various data manipulation tasks.

## Connecting IoT Applications to MongoDB

In the world of IoT, devices generate vast amounts of data that need to be stored and processed efficiently. MongoDB, with its flexible schema and scalability, is an ideal choice for storing sensor data, device information, and other IoT-related data. By integrating MongoDB into your IoT applications, you can leverage its powerful features to manage and analyze data in real-time.

### Why MongoDB for IoT?

1. **Flexible Schema:** IoT data can vary greatly in structure, and MongoDB's schema-less design allows for flexible data modeling without the need for predefined schemas.
2. **Scalability:** As your IoT network grows, MongoDB can scale horizontally to accommodate increasing data volumes.
3. **Rich Query Language:** MongoDB's powerful query language supports complex queries and aggregations, enabling sophisticated data analysis.

### Integrating MongoDB with a Python IoT Application

Let's walk through an example of how to connect a Python IoT application to MongoDB, perform data retrieval, and write data to the database using the `pymongo` library.

**Select the folder where you will create the project:**
• Navigate (or create first) to the folder where your project will reside.
```bash
cd <path_to_your_folder>
```

**Create the virtual environment:**
• run the venv command.
```bash
python -m venv .venv
```
• where .venv is the folder that will be created to hold all the elements required to run the virtual environment. We're prepending a . in front of the name to follow Linux conventions on hidden folders and files.

**Activate the virtual environment:**
• Activate the virtual environment, on Windows it should be:
```bash
./.venv/Scripts/Activate.ps1
```
• On Linux the command should be:
```bash
source ./.venv/bin/activate
```
• After that we're all set to install our modules and write the code.

**Installing `pymongo`:**
• First, ensure you have `pymongo` installed in your Python environment:
```bash
pip install pymongo
```

**Connecting to MongoDB:**
• Establish a connection to the MongoDB server.
```python
from pymongo import MongoClient

# Replace with your MongoDB connection string
client = MongoClient("mongodb://admin:password@localhost:27017/")

# Access the database
db = client.iot_database
```

**Writing Data to MongoDB:**
• Insert sensor data into a collection.
```python
sensor_data = {
    "device_id": "sensor_001",
    "timestamp": "2024-06-01T12:00:00Z",
    "temperature": 22.5,
    "humidity": 60
}

# Insert the document into the collection
db.sensor_data.insert_one(sensor_data)
```

**Retrieving Data from MongoDB:**
• Query the database for sensor data.
```python
# Find a single document
sensor_record = db.sensor_data.find_one({"device_id": "sensor_001"})
print(sensor_record)

# Find multiple documents with a filter
recent_data = db.sensor_data.find({"temperature": {"$gt": 20}})
for record in recent_data:
    print(record)
```

### Advantages of Using Programming Libraries

Integrating MongoDB operations directly into your application via programming libraries like `pymongo` offers several benefits:

1. **Seamless Integration:** Connect to MongoDB from within your application, allowing for real-time data storage and retrieval.
2. **Automation:** Automate data management tasks such as data insertion, updates, and queries, enhancing efficiency.
3. **Scalability:** Easily scale your application to handle more data as your IoT network grows.
4. **Flexibility:** Use the rich features of MongoDB's query language and indexing to perform complex data operations and analysis.

By leveraging MongoDB within your IoT applications, you can build robust, scalable solutions that efficiently handle large volumes of diverse data.

## Conclusion

In this blog post, we've explored the powerful combination of Docker and MongoDB, demonstrating how these tools can streamline your IoT development projects. Here are the key points we covered:

1. **Introduction to MongoDB and Docker:** We introduced MongoDB as a versatile NoSQL database and Docker as a robust containerization platform, highlighting their benefits for IoT applications.

2. **Advantages of Using Docker for MongoDB:** We discussed the portability, scalability, and ease of setup that Docker provides, making it an excellent choice for deploying MongoDB locally.

3. **Setting Up Docker:** Detailed instructions on installing Docker across various operating systems to get you started.

4. **Pulling MongoDB Docker Image:** We guided you through the process of pulling the official MongoDB image from Docker Hub.

5. **Running MongoDB Container:** We explained how to create and run a MongoDB container, including configuring ports, volumes, and environment variables.

6. **Accessing MongoDB Container:** We showed you how to access the MongoDB database inside the Docker container using the MongoDB shell and a MongoDB client.

7. **Data Persistence:** We emphasized the importance of data persistence and demonstrated how to use Docker volumes to persist MongoDB data.

8. **Basic MongoDB Operations:** We provided examples of essential MongoDB operations, including creating databases and collections, inserting documents, querying data, and updating documents.

9. **Connecting IoT Applications to MongoDB:** We discussed how IoT applications can leverage MongoDB to store and manage sensor data and other IoT-related information, complete with Python code examples.

MongoDB and Docker together offer a flexible, scalable, and efficient way to manage IoT data. By integrating these tools into your development projects, you can build robust applications capable of handling the complex and dynamic nature of IoT environments.

I encourage you to further explore MongoDB and Docker, experimenting with their features and capabilities. As you delve deeper, you'll discover even more ways to optimize and enhance your IoT solutions. Happy coding!

---

**Tags:** IoT, MongoDB, Docker, Python, Programming

**About the Author:** Jorge B. Aspiazu is an Electrical Engineer with a passion for technology, especially for programming languages.

---

## Recent Updates

### FastAPI Lifespan Event Handler Migration

**Date:** July 24, 2025

We have updated the FastAPI application to use the modern `lifespan` event handler instead of the deprecated `@app.on_event("startup")` method. This change ensures compatibility with newer versions of FastAPI and eliminates deprecation warnings.

#### What Changed:

**Before (Deprecated):**
```python
from fastapi import FastAPI
from app.server.models.database import init_db

api_app = FastAPI()

@api_app.on_event("startup")
async def start_db():
    await init_db()
```

**After (Modern Approach):**
```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.server.models.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await init_db()
    yield
    # Shutdown (if needed)

api_app = FastAPI(lifespan=lifespan)
```

#### Benefits of the Update:

1. **Future-proof:** Uses current FastAPI best practices
2. **No deprecation warnings:** Eliminates the "on_event is deprecated" warning
3. **Better resource management:** Explicit startup/shutdown lifecycle management
4. **Cleaner code:** Single function handles both startup and shutdown events
5. **Extensible:** Easy to add shutdown cleanup code if needed

This update ensures our application follows modern FastAPI patterns and maintains compatibility with future versions of the framework.


