from src.database.models import Project


def test_project_model():

    project = Project(
        name="Demo",
        description="Testing",
        owner_id=1
    )


    assert project.name == "Demo"
    assert project.owner_id == 1