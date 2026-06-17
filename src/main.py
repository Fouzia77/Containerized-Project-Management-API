from fastapi import FastAPI

from src.database.database import engine
from src.database.models import Base

from src.api.auth import router as auth_router
from src.api.projects import router as project_router
from src.api.tasks import router as task_router
from src.api.users import router as user_router



# Create tables
Base.metadata.create_all(bind=engine)



app = FastAPI(
    title="Containerized Project Management API",
    description="Project and Task Management API with JWT Authentication",
    version="1.0.0"
)



# Routers

app.include_router(
    auth_router
)

app.include_router(
    user_router
)

app.include_router(
    project_router
)

app.include_router(
    task_router
)



@app.get("/")
def root():

    return {
        "message": "Project Management API running"
    }