from sqlalchemy.orm import Session

from src.database.models import Task



def create_task(
    db:Session,
    title:str,
    description:str,
    status:str,
    project_id:int
):

    task = Task(
        title=title,
        description=description,
        status=status,
        project_id=project_id
    )


    db.add(task)
    db.commit()
    db.refresh(task)

    return task




def get_tasks(
    db:Session,
    project_id:int
):

    return db.query(Task).filter(
        Task.project_id == project_id
    ).all()




def get_task(
    db:Session,
    task_id:int
):

    return db.query(Task).filter(
        Task.id == task_id
    ).first()




def delete_task(
    db:Session,
    task
):

    db.delete(task)
    db.commit()

    return True

def update_task(
    db,
    task,
    title,
    description,
    status
):

    task.title = title
    task.description = description
    task.status = status

    db.commit()
    db.refresh(task)

    return task