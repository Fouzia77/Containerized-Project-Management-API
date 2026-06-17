from pydantic import BaseModel
from src.database.models import TaskStatus



class TaskCreate(BaseModel):

    title: str
    description: str | None = None
    status: TaskStatus = TaskStatus.TODO



class TaskUpdate(BaseModel):

    title: str | None = None
    description: str | None = None
    status: TaskStatus | None = None



class TaskResponse(BaseModel):

    id:int
    title:str
    description:str | None
    status:TaskStatus
    project_id:int


    class Config:
        from_attributes = True