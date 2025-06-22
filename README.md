# Time Series with Python & MongoDB

Learn the fundamental techniques for analyzing time-series data with Python, MongoDB, PyMongo, Pandas, & Matplotlib

*References*
- Blog post *(coming soon)*
- Video *(coming soon)* 

*Prerequisites*
- Python 3.8+ Installed
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) Installed (for local MongoDB instance)
- Terminal or PowerShell experience


## Getting Started

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

docker compose down  

# docker compose down -v
```

