from fastapi import FastAPI, HTTPException
from models import JobApplication
from file_handler import load_data, save_data

app = FastAPI()

# Load applications from file when server starts
applications = load_data()

@app.post("/applications/")
def add_application(app_data: JobApplication):
    if app_data.name in applications:
        raise HTTPException(status_code=400, detail="Application already exists")
    
    # Save new application
    applications[app_data.name] = app_data.dict()
    save_data(applications)
    return {"message": "Application added"}

@app.get("/applications/")
def get_applications():
    return applications

@app.get("/applications/search")
def search_applications(status: str):
    """Search applications by status"""
    return {name: data for name, data in applications.items() if data["status"] == status}
