from pydantic import BaseModel


class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    status: str = "active"


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: str | None
    status: str

    class Config:
        from_attributes = True