from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="Portfolio API",
    description="Backend API for portfolio website",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class Project(BaseModel):
    id: int
    title: str
    description: str
    tech: List[str]
    category: str

class ContactMessage(BaseModel):
    name: str
    email: str
    message: str

# Sample data
projects = [
    {
        "id": 1,
        "title": "Task Management API",
        "description": "A robust RESTful API built with Flask and PostgreSQL for managing tasks, users, and projects.",
        "tech": ["Flask", "PostgreSQL", "SQLAlchemy", "JWT", "REST API"],
        "category": "Backend"
    },
    {
        "id": 2,
        "title": "E-commerce API",
        "description": "High-performance e-commerce backend built with FastAPI.",
        "tech": ["FastAPI", "PostgreSQL", "Pydantic", "OpenAPI", "AsyncIO"],
        "category": "Backend"
    },
    {
        "id": 3,
        "title": "Image Classification ML Model",
        "description": "Deep learning model for image classification using Convolutional Neural Networks.",
        "tech": ["TensorFlow", "Keras", "CNN", "Python", "NumPy"],
        "category": "AI/ML"
    },
    {
        "id": 4,
        "title": "Sales Analytics Dashboard",
        "description": "Comprehensive data science project analyzing sales data with interactive visualizations.",
        "tech": ["Pandas", "Matplotlib", "Seaborn", "Jupyter", "Scikit-learn"],
        "category": "Data Science"
    },
]

@app.get("/")
async def root():
    return {"message": "Portfolio API is running"}

@app.get("/api/projects", response_model=List[Project])
async def get_projects():
    return projects

@app.get("/api/projects/{project_id}", response_model=Project)
async def get_project(project_id: int):
    project = next((p for p in projects if p["id"] == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

@app.post("/api/contact")
async def send_message(message: ContactMessage):
    # In production, this would send an email or save to database
    return {
        "status": "success",
        "message": "Thank you for your message! I will get back to you soon."
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)



