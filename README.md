# Udemy: MongoDB Database Developer Course In Python  
<https://www.udemy.com/course/mongodb-database-developer-course-in-python/?couponCode=KEEPLEARNING>  

# Udemy: Master MongoDB Development Applications  
MongoDB with Python, MongoDB with Django, MongoDB with NodeJs, etc.  
<https://www.udemy.com/course/mongodb-mastering-mongodb-for-beginners-theory-projects/learn/lecture/28067330#overview>  

# Udemy: Complete MongoDB Administration Guide   
Master MongoDB database using JavaScript Mongo Shell, Robo 3T (Robomongo) and MongoDB Compass 
Bogdan Stashchuk 
<https://www.udemy.com/course/mongodb-essentials-m/?couponCode=KEEPLEARNING>   





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

# TODO: Openmeteo API MongoDB  
