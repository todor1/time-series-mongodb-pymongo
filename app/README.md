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
