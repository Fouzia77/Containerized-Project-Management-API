from sqlalchemy.orm import Session

from src.database.models import Project


def create_project(
    db: Session,
    name: str,
    description: str,
    owner_id: int
):

    project = Project(
        name=name,
        description=description,
        owner_id=owner_id
    )


    db.add(project)
    db.commit()
    db.refresh(project)

    return project



def get_projects(
    db: Session,
    user_id:int
):

    return db.query(Project).filter(
        Project.owner_id == user_id
    ).all()



def get_project(
    db:Session,
    project_id:int,
    user_id:int
):

    return db.query(Project).filter(
        Project.id == project_id,
        Project.owner_id == user_id
    ).first()



def delete_project(
    db:Session,
    project
):

    db.delete(project)
    db.commit()

    return True

def update_project(
    db,
    project,
    name,
    description
):
    project.name = name
    project.description = description

    db.commit()
    db.refresh(project)

    return project