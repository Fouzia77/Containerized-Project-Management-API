from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from src.database.database import Base
import enum


class TaskStatus(str, enum.Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"



class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True,
        nullable=False
    )

    hashed_password = Column(
        String,
        nullable=False
    )

    is_active = Column(
        Boolean,
        default=True
    )


    projects = relationship(
        "Project",
        back_populates="owner",
        cascade="all, delete"
    )



class Project(Base):

    __tablename__ = "projects"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    description = Column(
        String,
        nullable=True
    )


    owner_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )


    owner = relationship(
        "User",
        back_populates="projects"
    )


    tasks = relationship(
        "Task",
        back_populates="project",
        cascade="all, delete"
    )



class Task(Base):

    __tablename__ = "tasks"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    title = Column(
        String,
        nullable=False
    )


    description = Column(
        String,
        nullable=True
    )


    status = Column(
        Enum(TaskStatus),
        default=TaskStatus.TODO
    )


    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )


    project = relationship(
        "Project",
        back_populates="tasks"
    )