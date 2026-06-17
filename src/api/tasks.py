from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.database import get_db
from src.database.models import User

from src.core.dependencies import get_current_user

from src.services.task_service import (
    create_task,
    get_tasks,
    get_task,
    delete_task,
    update_task
)

from src.services.project_service import get_project


router = APIRouter(
    prefix="/api",
    tags=["Tasks"]
)



# Create task for project
@router.post(
    "/projects/{project_id}/tasks",
    status_code=201
)
def add_task(
    project_id:int,
    title:str,
    description:str=None,
    status:str="TODO",
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


    return create_task(
        db,
        title,
        description,
        status,
        project_id
    )




# Get project tasks
@router.get(
    "/projects/{project_id}/tasks"
)
def list_tasks(
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


    return get_tasks(
        db,
        project_id
    )




# Get single task
@router.get(
    "/tasks/{task_id}"
)
def get_one_task(
    task_id:int,
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    task = get_task(
        db,
        task_id
    )


    if not task:
        raise HTTPException(
            404,
            "Task not found"
        )


    project = get_project(
        db,
        task.project_id,
        user.id
    )


    if not project:
        raise HTTPException(
            403,
            "Not allowed"
        )


    return task




# Delete task
@router.delete(
    "/tasks/{task_id}"
)
def remove_task(
    task_id:int,
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    task = get_task(
        db,
        task_id
    )


    if not task:
        raise HTTPException(
            404,
            "Task not found"
        )


    project = get_project(
        db,
        task.project_id,
        user.id
    )


    if not project:
        raise HTTPException(
            403,
            "Not allowed"
        )


    delete_task(
        db,
        task
    )


    return {
        "message":"Task deleted"
    }

@router.put("/tasks/{task_id}")
def edit_task(
    task_id:int,
    title:str,
    description:str=None,
    status:str="TODO",
    db:Session=Depends(get_db),
    user:User=Depends(get_current_user)
):

    task = get_task(db, task_id)

    if not task:
        raise HTTPException(404,"Task not found")


    project = get_project(
        db,
        task.project_id,
        user.id
    )

    if not project:
        raise HTTPException(
            403,
            "Not allowed"
        )


    return update_task(
        db,
        task,
        title,
        description,
        status
    )