# Udemy: MongoDB Database Developer Course In Python  
<https://www.udemy.com/course/mongodb-database-developer-course-in-python/?couponCode=KEEPLEARNING>  

# Udemy: Master MongoDB Development Applications  
MongoDB with Python, MongoDB with Django, MongoDB with NodeJs, etc.  
<https://www.udemy.com/course/mongodb-mastering-mongodb-for-beginners-theory-projects/learn/lecture/28067330#overview>  

# Udemy: Complete MongoDB Administration Guide   
Master MongoDB database using JavaScript Mongo Shell, Robo 3T (Robomongo) and MongoDB Compass 
Bogdan Stashchuk 
<https://www.udemy.com/course/mongodb-essentials-m/?couponCode=KEEPLEARNING>   


# TODO: Openmeteo API MongoDB  


# CFE: Time Series with Python & MongoDB

Learn the fundamental techniques for analyzing time-series data with Python, MongoDB, PyMongo, Pandas, & Matplotlib

*References*
- Blog post *(coming soon)*
- Video *(coming soon)* 

*Prerequisites*
- Python 3.8+ Installed
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) Installed (for local MongoDB instance)
- Terminal or PowerShell experience

<https://github.com/codingforentrepreneurs/time-series-mongodb-pymongo/tree/main>  

<https://github.com/codingforentrepreneurs/time-series-mongodb-pymongo/tree/final>  


## 1.Getting Started

1. Make a project directory
```
mkdir -p ~/dev/ts-pymongo
cd ~/dev/ts-pymongo
```
2. Clone this repo:

```
git clone https://github.com/codingforentrepreneurs/time-series-mongodb-pymongo .
```

3. Make and activate a virtual environment:


```
python3.10 -m venv venv
```


*macOS/Linux activation*
```
source venv/bin/activate
```

*Windows activation*
```
./venv/Scripts/activate
```

4. Upgrade Virtual Environment Pip
```
(venv) python -m pip install pip --upgrade
```

5. Move `src/example.env` to `src/.env`
```
mv src/example.env src/.env
```

6. Change `MONGO_INITDB_ROOT_PASSWORD` in `.env`
Create a new password with:

```
(venv) python -c "import secrets;print(secrets.token_urlsafe(32))"
```

So `.env` looks like:

```
MONGO_INITDB_ROOT_USERNAME="root"
MONGO_INITDB_ROOT_PASSWORD="wlke0lL-v7FkGFn5Cl0brfxHJqhDPImBmg-MRfCIXx4" 
```

7. Install requirements

```
(venv) python -m pip install -r src/requirements.txt
```

8. Run Docker Compose
Don't have docker? Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)

```
cd ~/dev/ts-pymongo
docker compose up
```


9. Checkout the Final Results
If you want to see the final code changes, checkout the `final` branch.
```
git checkout final
```

## 1 UV Python Project Setup   

```bash
python.exe -m pip install --upgrade pip  
pip install -r requirements.txt 
```

<https://blog.pecar.me/uv-with-django>

### 1.Initialize project  

uv init .

### 2.Create environment  

```bash
uv venv --python 3.13
uv venv envname
uv venv envname --python 3.12
```  

if toml file available/linux: 
```bash
uv venv
source .venv/Scripts/Activate
source .venv/bin/activate
uv pip install . --link-mode=copy
```

**NB: Check the .python-version file**
Copilot 
I have updated the .python-version file to specify version 3.13. 
The uv command was likely prioritizing the version specified in that file over the one provided in the command-line arguments. 
With this change, uv should now create a virtual environment with Python 3.13 as intended.

You can now try running your command again:
uv venv --python 3.13

### 3.Activate environment  
```bash
win
source .venv/Scripts/activate
source env/Scripts/activate
```

linux/mac
```bash
source .venv/bin/activate
```

### 4.Install packages  

```bash
uv pip install --upgrade pip
uv pip install -r requirements.txt
```

The quotes around the package specification are important to prevent shell interpretation of the ">" characters
```bash
uv pip install "Django>=5.2,<5.3"
```

### 5.UV Workflow  
```bash
uv init .
uv init proj_name
cd proj_name
uv venv --python 3.12
source .venv/Scripts/activate
uv pip install --upgrade pip
uv pip install -r requirements.txt
```

### 6 UV Migrating from Requirements  

Save dependencies to pyproject.toml:

```bash
uv init .
uv init proj_name
cd proj_name
uv venv --python 3.12
source .venv/Scripts/activate
uv add -r requirements.txt
uv lock
```

### 7 Docker Start   

```bash
docker compose up  
docker compose up --watch  

docker compose down  

# docker compose down -v
```

### 8 Git  

```bash
git remote -v

# Remove the Original Remote (forked source)
git remote remove origin

# Add Your Fork as the New Remote
git remote add origin https://github.com/todor1/time-series-mongodb-pymongo.git
# git remote add upstream https://github.com/todor1/time-series-mongodb-pymongo.git

# Push to Your Fork
# Use -u to set the upstream so future pushes can be done with just git push.
git push -u origin main

# Then you can fetch and merge changes from the original repo like this:
# git fetch upstream
# git merge upstream/main  
# git push origin main

```


## 2.Project First Steps  
```bash
python -i src/db_client.py

client = get_db_client()

# below should return the same id even if multiple client calls above
id(client)

data = {"hello":"world", "order":1}
data = {"hello":"world", "order":2}
data = {"hello":"world", "order":3}

db = client.hello

collection = db.world

# not able to store the same pointer, but possible to store same data as another object
collection.insert_one(data)

list(collection.find())

result = collection.insert_one(data)
print(result.acknowledged)
print(result.inserted_id)
```

## 3.Check Data after Insert  

```bash
python -i src/db_client.py
client = get_db_client()
db = client.business
collection = db.rating_over_time
collection.find()
len(list(collection.find()))
```

## 4.Aggregate Data  

```bash
python -i src/db_client.py
client = get_db_client()
db = client.business
collection = db.rating_over_time
collection.find()
len(list(collection.find()))
# list(collection.find())  -> prints multiple datasets

# arbitrary cuisine arguments
results = list(
    collection.aggregate([
        {
        "$group": {
            "_id": {"cuisine":"abc"},
            }   
        }])
)
print(len(results))
print(results)

list(collection.find())[0]

results = list(
    collection.aggregate([
        {
        "$group": {
            "_id": {"cuisine":"$metadata"},
            }   
        }])
)
print(len(results))

results = list(
    collection.aggregate([
        {
        "$group": {
            "_id": {"cuisine":"$metadata.cuisine"},
            }   
        }])
)
print(len(results))

results = list(
    collection.aggregate([
        {
        "$group": {
            "_id": {"cuisine":"$metadata.cuisine"},
            "count": {"$sum":1},
            }   
        }])
)
print(results)

results = list(
    collection.aggregate([
        {
        "$group": {
            "_id": {"cuisine":"$metadata.cuisine"},
            "count": {"$sum":1},
            "average": {"$avg":"$rating"},
            }   
        }])
)

```

## 5.Modifying Incoming Doc Data  

```bash
python -i src/db_client.py
client = get_db_client()
db = client.business
collection = db.rating_over_time
collection.find()
len(list(collection.find()))
##################################

results = list(
    collection.aggregate([
        {
            "$project": {
                "date":{
                    "$dateToString": {"format":"%Y-%m", "date": "$timestamp"}
                }
            }
        }
    ])
)

print(len(results))
```

## 6.Time Series Aggregations  

```bash
python -i src/db_client.py
client = get_db_client()
db = client.business
collection = db.rating_over_time
len(list(collection.find()))
##################################

results = list(
    collection.aggregate([
        {
            "$project": {
                "date":{
                    "$dateToString": {"format":"%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
                }
        },
        {
            "$group": {               
                "_id": { 
                    "cuisine": "$cuisine",
                    "date": "$date"},
                "avg": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine"}},
        {"$addFields": {"date": "$_id.date"}},
    ])
)

print(len(results))
```

## 7.Match Filter & Sorting on Aggregations    

### Sort  
 - {"$sort": {"date": 1}} -> oldest to newest
 - {"$sort": {"date": -1}} -> newest to oldest

```python
results = list(
    collection.aggregate([
        {
            "$project": {
                "date":{
                    "$dateToString": {"format":"%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
                }
        },
        {
            "$group": {               
                "_id": { 
                    "cuisine": "$cuisine",
                    "date": "$date"},
                "avg": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine"}},
        {"$addFields": {"date": "$_id.date"}},
        {"$sort": {"date": 1}},
    ])
)

results[:10]

results[-10:] 

```

### Filter/Match

Filter the whole object by dates before sorting and applying aggregations  

```python
import datetime 

results = list(
    collection.aggregate([
        {
            "$match": {
                "timestamp": {
                    "$gte": datetime.datetime.now() - datetime.timedelta(days=50), 
                    "$lte": datetime.datetime.now()}
            }
        },
        {
            "$project": {
                "date":{
                    "$dateToString": {"format":"%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
                }
        },
        {
            "$group": {               
                "_id": { 
                    "cuisine": "$cuisine",
                    "date": "$date"},
                "avg": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine"}},
        {"$addFields": {"date": "$_id.date"}},
        {"$sort": {"date": -1}},
    ])
)

results[:10]

```

## 8.Pandas & MongoDB  


```python
import pandas as pd

dataset = list(
    collection.aggregate([        
        {
            "$project": {
                "date":{
                    "$dateToString": {"format":"%Y-%m", "date": "$timestamp"}
                },
                "cuisine": "$metadata.cuisine",
                "rating": "$rating",
                }
        },
        {
            "$group": {               
                "_id": { 
                    "cuisine": "$cuisine",
                    "date": "$date"},
                "average": {"$avg": "$rating"}
            }
        },
        {"$addFields": {"cuisine": "$_id.cuisine"}},
        {"$addFields": {"date": "$_id.date"}},
        {"$sort": {"date": 1}},
    ])
)

df = pd.DataFrame(dataset)
df["date"] = pd.to_datetime(df["date"])
df = df[["date", "cuisine", "average"]]
df.set_index("date", inplace=True)
df.head().round(2)
```

# Blog TS+MongoDB  

**Time Series with Python & MongoDB Guide**  
<https://www.codingforentrepreneurs.com/blog/time-series-with-python-mongodb-guide>  

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
git commit -m "Add blog post content and project updates"
```

### 5. Push to Remote and Set Upstream
```bash
git push -u origin blog-post
```

The `-u` flag sets the upstream tracking, so future pushes from this branch can be done with just `git push`.

### Alternative: Check Current Branch Only
```bash
# To see which branch is currently active
git branch --show-current
```

## Step 1: Create Project Directory  

```bash
# Create a directory for all projects:
# mkdir -p ~/Dev

# Create your project directory
# mkdir -p ~/Dev/ts-pymongo

# Setup VS Code Workspace (optional)
echo "" > ts-pymongo.workspace
```

In ~/Dev/ts-pymongo/ts-pymongo.workspace add:
```json
{
  "folders": [
    {
      "path": "."
    }
  ],
  "settings": {}
}
```

## Step 2: Docker Compose Configuration  
In this step, we're going to use a local instance of MongoDB by leveraging Docker. The only reason to do it this way is to learn how to leverage MongoDB in your projects. Once you learn, using a managed MongoDB database is highly recommended so be sure to check out MongoDB on Linode when you're ready for production.
Assuming you have Docker Desktop installed and at least one of the following commands work:
 - docker compose version
 - docker-compose version
If either of the above commands do not work, consider using a managed instance on Linode right now.
Docker Compose configuration
In ~/Dev/ts-pymongo/, we'll add the following:
 - src/.env
 - docker-compose.yaml  

First, ~/Dev/ts-pymongo/docker-compose.yaml: 
```yaml
version: '3.9'

services:
  mongo:
    image: mongo
    restart: always
    ports: 
      - 27017:27017
    env_file: ./src/.env
```  

Let's add our environment variables for this to work:
```bash
mkdir -p ~/Dev/ts-pymongo/src
echo "" > ~/Dev/ts-pymongo/src/.env
```

I create passwords like this with: 
```bash
python -c "import secrets;print(secrets.token_urlsafe(32))"
```

Docker & MongoDB Environment Variables When spinning up MongoDB in Docker or Docker compose we need to set the following enviroNment variables:
 - MONGO_INITDB_ROOT_USERNAME
 - MONGO_INITDB_ROOT_PASSWORD
This is defined in the Official MongoDB Docker Image on [DockerHub](https://hub.docker.com/_/mongo/). 

**Docker Compose Commands**
There are 3 important commands we need to know for this project:
 - docker compose up -d: runs the database in the background
 - docker compose down: turns off the database; keeps data
 - docker compose down -v: removes the database; deletes data
It's true there's a lot more to Docker and Docker Compose than this but we'll save those details for another time  

```bash
# runs the database in the background
docker compose up -d

# turns off the database; keeps data
docker compose down 

# removes the database; deletes data
docker compose down -v
```

## Step 3: Create your Python Virtual Environment  

Isolate your python projects by leveraging virtual environments. There are many ways to accomplish this but we'll use the built-in python package venv. 

I recommend you use the Python distribution directly from python.org. 
I do not recommend you use Anaconda, mini-conda, or any other Python distribution. Unofficial distributions, like Anaconda, can cause third-party dependency issues that are hard to diagnose which is why we're going to leave it out for now.  

tldr
```bash
mkdir -p ~/Dev/ts-pymongo/
cd ~/Dev/ts-pymongo/
python3.10 -m venv venv
```

If on Windows, use C:\Python310\python.exe instead of python3.10.
For a more detailed virtual environment creation, check the sections below. 
If the tldr above works for you, skip to Step 3.

macOS/Linux Virtual Environment Creation

cd ~/Dev/ts-pymongo/
python3.10 -m venv venv

Notice that we used venv twice? The first -m venv is calling the python module. The second venv is what we're naming our virtual environment and venv is a conventional name.
```bash
# Activate it
source venv/bin/activate

# Update pip
$(venv) python -m pip install pip --upgrade
```

Using python -m pip is the recommended method of handling pip installations. Using pip without python -m might cause system-wide dependency issues.

Deactivate and Reactivate
```bash
$(venv) deactivate
source venv/bin/activate
```

Activation-less Commands If you prefer to not activate your virtual environment, that's okay.  
You'll just need to leverage venv/bin/ and related items. 
So you can use the virtual environment python with: 

```bash
venv/bin/python --version

# Or, for example, if you're using the Python package uvicorn, you can call:

venv/bin/uvicorn

# You can also use paths like:
~/Dev/ts-pymongo/venv/bin/uvicorn
# or
/Users/cfe/Dev/ts-pymongo/venv/bin/uvicorn
```

Replace cfe as your username of course.
Now you're ready for the next step.
Windows Virtual Environment Creation

cd ~/Dev/ts-pymongo/
C:\Python310\python.exe -m venv venv

C:\Python310\python.exe
assumes this is the location where you installed Python.3.10. If you did not install it here, you'll need to locate the exact place you did install it before you create your virtual environment.
One way to do that is to open up PowerShell (after you installed Python) and run:
```bash
python

# This will either cause an error or it will enter the Python shell.

import os
import sys
print(os.path.dirname(sys.executable))
```
This will yield something like:

C:\Python38
Whatever path os.path.dirname(sys.executable) yields you'll have to add python.exe to it in order to use python.
For example, above yielded C:\Python38 and not C:\Python310. In that case you would use:

C:\Python38\python.exe -m venv venv
To create your virtual environment.
Notice that we used venv twice? The first -m venv is calling the python module. The second venv is what we're naming our virtual environment and venv is a conventional name.
Activate it

./venv/Scripts/activate
This will yield something like:

(venv) PS C:\Users\cfe\Dev\ts-pymongo>
We'll use $(venv) to denote an activated virtual environment going forward.
Update pip

$(venv) python -m pip install pip --upgrade
Using python -m pip is the recommended method of handling pip installations. Using pip without python -m might cause system-wide dependency issues.
Deactivate and Reactivate

$(venv) deactivate
./venv/Scripts/activate
Activation-less Commands If you prefer to not activate your virtual environment, that's okay. You'll just need to leverage venv/bin/ and related items.
So you can use the virtual environment python with:

venv/Scripts/python --version
Or, for example, if you're using the Python package uvicorn, you can call:

venv/Scripts/uvicorn
You can also use paths like:

~/Dev/ts-pymongo/venv/Scripts/uvicorn
or

C:\Users\cfe\Dev\ts-pymongo\venv\Scripts\uvicorn
Replace cfe with your username of course. Also, as you may know, PowerShell can use either forward slash / or backslash \.
Now you're ready for the next step.

## Step 4. Connect Python to MongoDB  

At this point, we have the following available to us:
A Python Virtual Environment
A Running MongoDB instance
Now it's time to connect Python to MongoDB
1. Install Python Requirements
Activate our virtual environment

```bash
source .venv/Scripts/activate
```

Create requirements.txt
```bash
echo "" > src/requirements.txt
echo "pymongo" >> src/requirements.txt
echo "python-decouple" >> src/requirements.txt
echo "pandas" >> src/requirements.txt
echo "matplotlib" >> src/requirements.txt
``` 

- pymongo (Docs) is the primary package we'll use to connect Python with MongoDB.
- python-decouple (Docs) is a neat way to load .env secrets/configuration into our Python project.
- pandas (Docs) is powerful way to work with datasets. We'll use it for exporting our time series plots.
- matplotlib. (Docs) Pandas requires matplotlib to create charts and graphs.

Install requirements  
```bash
uv add -r src/requirements.txt
python -m pip install pip --upgrade
python -m pip install -r src/requirements.txt
```

Create db_client.py In src/db_client.py add:

```python
from functools import lru_cache

import decouple
from pymongo import MongoClient

@lru_cache
def get_db_client(host='localhost'):
    mongodb_un = decouple.config("MONGO_INITDB_ROOT_USERNAME")
    mongodb_pw = decouple.config("MONGO_INITDB_ROOT_PASSWORD")
    mongodb_host = decouple.config("MONGO_HOST", default='localhost')
    db_url =  f"mongodb://{mongodb_un}:{mongodb_pw}@{mongodb_host}:27017"
    return MongoClient(db_url)
```

**Let's break this down:**
 - lru_cache makes calling get_db_client a little more efficient during the same session. In other words, get_db_client will only create 1 instance of MongoClient which is exactly what we want if we turn this into a full web application.
 - decouple.config allows us to use our configuration from .env
 - get_db_client creates a Python MongoDB Client that connects to our Docker-based MongoDB.
 - MongoClient takes in the database url which ends up looking like MongoClient("mongodb://username:password@host:port"). MongoDB typically uses port 27017 which is why we have that port listed here. If you used a managed mongodb service, chances are good you will have to update the host by setting MONGO_HOST in .env.  

## Step 5. Basic CRUD with PyMongo 

Here's the process to leveraging CRUD in PyMongo:
1. Connect to your MongoDB Client
1. Select a Database
1. Select a Collection
1. Use CRUD operations

Navigate in src and run the following:

```bash
cd src
python

# 1.Connect to your MongoDB Client
import db_client
client = db_client.get_db_client()

# 2. Select a Database
db = client.business

# 3. Select a Collection
collection = db["ratings"]

# Let's verify what's in this collection
list(collection.find())
```

If you just started this one, you should see [] as your response.
Before we jump into the CRUD operations, let's break down what just happened.
 - client = db.get_db_client() initializes a connection to MongoDB
 - db = client.business declares a database to use
 - collection = db["ratings"] declares a collection to use  
  

If you're coming from SQL, you might be wondering:
 - Where is the command to create the database?
 - What is a collection? Is it a table?
 - Where is the command to create the collection?
 - When do we declare the fields we want to enforce in the collection?  

A simple answer to these questions are: that's not how MongoDB works. Databases are groups of collections and collections of groups of documents. 

These documents have incredible flexibility and can look a bit like this:
 - {"product": "sparkling water", "price": 1.99}
 - {"location": "Austin, Texas", "ranch_living": True}

Both of these documents resemble dictionaries in Python and objects in JavaScript; and that's exactly the point.  

With documents, the field names (ie keys) do not matter to storing the document. As the developer, you can enforce rules for field names but it's not required.  

I think this is pretty neat and leaves the option for adding new data (including nested dictionaries/objects) whenever you need to.

```bash
# 4. Add Data as a Document to a Collection
# This is beyond simple. Here's how it's done:

# client = db.get_db_client()
# db = client.business
# collection = db["ratings"]

data_document = {"name": "Torchy's Tacos", "location": "Austin, Texas", "rating": 4.5}
collection.insert_one(data_document)  

# Another way:
db = client.business
rating_data = {"name": "Gourdough's Big. Fat. Donuts.", "location": "Austin, Texas", "rating": 5.0}
db["ratings"].insert_one(rating_data)

# 5. List Data from Collection Now that we added two documents, we can list them out in the following ways:

db = client.business
list(db["ratings"].find())

# or
db = client.business
collection = db["ratings"]
list(collection.find())
```

the .find() method on a collection also allows for querying the data such as: 
```python
for obj in collection.find({"name": "Torchy's Tacos"}):
    print(obj)
```

6. Get a Single Document from a Collection
Looking back on our data, we see that _id is set with an ObjectId() class. This _id is unique to the document and it's something we can use for lookups (especially to edit or delete items).
First let's get a document using the find_one method on our collection:

```python
document_result = collection.find_one({"name": "Torchy's Tacos"})
document_result
```  

Notice that find_one in PyMongo maps to the findOne method in MongoDB (docs). Python uses snake_case so be sure to try snake_case if you ever find a method that doesn't seem to work.
In this case, our document_result could yield None if our query yields no results. It's important to note that querying in MongoDB can get really complex so we'll leave that for another time. Let's get back to getting the value of the _id.  

```python
document_result = collection.find_one({"name": "Torchy's Tacos"})
object_id = None
if document_result is not None:
    object_id = document_result['_id']
print(object_id)
``` 

Now that we have an Object Id for a document, let's look it up:

```python
from bson.objectid import ObjectId

if isinstance(object_id, str):
    object_id = ObjectId(object_id)
result = collection.find_one({"_id": object_id})
print(result)
```

7. Update a Single Document from a Collection  

First, let's start with our object_id since it's unique for any given document.  

```python
object_id = ObjectId(object_id)

# Now, let's get new data:
new_data = {"cuisine": "Mexican", "only_location": False, "total_visitor_count": 120_000}

# To update, we're going to combine a query (in our case the object_id) as well as the data we want to change (using $set):
query_filter = {"_id": object_id}
update_data = {"$set": new_data}
collection.update_one(query_filter, update_data)
```

Notice that we nested our new_data instead of another dictionary with the key $set. This will literally set the values within our document based on whatever is in new_data. You can use dot notation for setting data but that's outside the scope of what we're doing here.
Now we're going to increment a field in our data.
Above we set total_visitor_count to 120_000 (stored as 120000). This is the same thing as replacing the original value with our new value.
But what if we wanted to do some math on this field? Let's see how it's done with the $inc operator:
Add 500 visitors*  

```bash
increment_data = {"$inc": {"total_visitor_count": 500}}
collection.update_one(query_filter, update_data)
```

Or
Subtract 293 by adding -293 visitors*

```bash
decrement_data = {"$inc": {"total_visitor_count": -293}}
collection.update_one(query_filter, update_data)
```

So both $set and $inc are incredibly useful for updating the data stored within a document. $inc is especially useful when you're dealing with storing integers or floats. Read more about $inc here and more about $set here as well as all other filed update operators here.  

7. Delete a Single Document from a Collection  
Let's create, update, and delete on this one: 

```python  

# Setup  
import db_client
client = db.get_db_client()
db = client.business
collection = db["ratings"]

# Create
data = {'name': "CFE Tacos", 'location': 'Austin, Texas', 'rating': 5}
result = collection.insert_one(data)
object_id = result.inserted_id
object_id

# Update 
data = {'name': "Just-in-Time Tacos"}
collection.update_one({"_id": object_id}, {"$set": data})
new_visitors_data = {'visitors': 300_000}
collection.update_one({"_id": object_id}, {"$inc": new_visitors_data})
new_visitors_data_again = {'visitors': 320_120}
collection.update_one({"_id": object_id}, {"$inc": new_visitors_data_again})

# List Matching Data
list(collection.find({"name": "Just-in-Time Tacos"}))

# Retrieve New Data
stored_result = collection.find_one({"_id": object_id})
print(stored_result)

# Delete Listing
delete_result = collection.delete_one({"_id": object_id})
print(delete_result.deleted_count, delete_result.acknowledged, delete_result.raw_result)
```

Now that we understand some of the basics of MongoDB, let's start using Time Series data.

## Step 6. Generate Time Series Collection & Data  
Let's create a new collection that's designed for time series [docs](https://www.mongodb.com/docs/manual/core/timeseries-collections/):
  
We're going to add a new time series by using the create_collection method like this:  
```bash
name = "my_collection_name"
db.create_collection(
        name,
        timeseries= {
            "timeField": "timestamp",
            "metaField": "metadata",
            "granularity": "seconds"
        }
    )
```

