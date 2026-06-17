from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.database.models import User

from src.core.dependencies import get_current_user

from src.services.project_service import (
    create_project,
    get_projects,
    get_project,
    delete_project,
    update_project
)


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)



@router.post("", status_code=201)
def create(
    name: str,
    description: str = None,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    project = create_project(
        db,
        name,
        description,
        user.id
    )


    return project




@router.get("")
def list_projects(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    return get_projects(
        db,
        user.id
    )




@router.get("/{project_id}")
def get_one(
    project_id:int,
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    project = get_project(
        db,
        project_id,
        user.id
    )


    if not project:
        raise HTTPException(
            404,
            "Project not found"
        )


    return project




@router.delete("/{project_id}")
def remove(
    project_id:int,
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    project = get_project(
        db,
        project_id,
        user.id
    )


    if not project:
        raise HTTPException(
            404,
            "Project not found"
        )


    delete_project(
        db,
        project
    )


    return {
        "message":"Project deleted"
    }


@router.put("/{project_id}")
def update(
    project_id:int,
    name:str,
    description:str=None,
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    project = get_project(
        db,
        project_id,
        user.id
    )

    if not project:
        raise HTTPException(
            404,
            "Project not found"
        )

    return update_project(
        db,
        project,
        name,
        description
    )