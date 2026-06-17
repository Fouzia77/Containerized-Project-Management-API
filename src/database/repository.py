from sqlalchemy.orm import Session

from src.database.models import (
    User,
    Project,
    Task
)


# ---------------- USER REPOSITORY ----------------

class UserRepository:

    def __init__(self, db: Session):
        self.db = db


    def get_by_email(self, email: str):

        return self.db.query(User).filter(
            User.email == email
        ).first()



    def create(
        self,
        email: str,
        hashed_password: str
    ):

        user = User(
            email=email,
            hashed_password=hashed_password
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user



# ---------------- PROJECT REPOSITORY ----------------

class ProjectRepository:


    def __init__(self, db: Session):
        self.db = db



    def create(
        self,
        name,
        description,
        owner_id
    ):

        project = Project(
            name=name,
            description=description,
            owner_id=owner_id
        )

        self.db.add(project)
        self.db.commit()
        self.db.refresh(project)

        return project




    def get_all_by_owner(
        self,
        owner_id
    ):

        return self.db.query(Project).filter(
            Project.owner_id == owner_id
        ).all()




    def get_by_id(
        self,
        project_id
    ):

        return self.db.query(Project).filter(
            Project.id == project_id
        ).first()




    def delete(
        self,
        project
    ):

        self.db.delete(project)
        self.db.commit()




# ---------------- TASK REPOSITORY ----------------


class TaskRepository:


    def __init__(self, db: Session):
        self.db=db



    def create(
        self,
        title,
        description,
        status,
        project_id
    ):


        task = Task(
            title=title,
            description=description,
            status=status,
            project_id=project_id
        )


        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task




    def get_by_id(
        self,
        task_id
    ):

        return self.db.query(Task).filter(
            Task.id == task_id
        ).first()



    def get_by_project(
        self,
        project_id
    ):

        return self.db.query(Task).filter(
            Task.project_id == project_id
        ).all()




    def delete(
        self,
        task
    ):

        self.db.delete(task)
        self.db.commit()