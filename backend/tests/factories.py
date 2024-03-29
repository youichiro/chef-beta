from sqlalchemy.orm import Session

from app import models


def create_project_type(db: Session, **kwargs):
    project_type = models.ProjectType(name=kwargs.get("name", "tagging"))
    db.add(project_type)
    db.commit()
    return project_type


def create_project(db: Session, **kwargs):
    project_type_id = kwargs.get("project_type_id")
    if project_type_id is None:
        project_type = create_project_type(db)
        project_type_id = project_type.id

    project = models.Project(
        project_type_id=project_type_id,
        name=kwargs.get("name", "dummy project"),
    )
    db.add(project)
    db.commit()
    return project


def create_user(db: Session, **kwargs):
    user = models.User(name=kwargs.get("name", "dummy user"))
    db.add(user)
    db.commit()
    return user


def create_dataset(db: Session, **kwargs):
    project_id = kwargs.get("project_id")
    if project_id is None:
        project = create_project(db, project_type_id=kwargs.get("project_type_id"))
        project_id = project.id

    dataset = models.Dataset(
        project_id=project_id,
        name=kwargs.get("name", "dummy dataset"),
    )
    db.add(dataset)
    db.commit()
    return dataset


def create_guideline(db: Session, **kwargs):
    project_id = kwargs.get("project_id")
    if project_id is None:
        project = create_project(db, project_type_id=kwargs.get("project_type_id"))
        project_id = project.id

    guideline = models.Guideline(
        project_id=project_id,
        content=kwargs.get("content", "dummy guideline content"),
    )
    db.add(guideline)
    db.commit()
    return guideline


def create_project_member(db: Session, **kwargs):
    project_id = kwargs.get("project_id")
    if project_id is None:
        project = create_project(db, project_type_id=kwargs.get("project_type_id"))
        project_id = project.id

    member_id = kwargs.get("member_id")
    if member_id is None:
        user = create_user(db)
        member_id = user.id

    project_member = models.ProjectMember(
        project_id=project_id,
        member_id=member_id,
    )
    db.add(project_member)
    db.commit()
    return project_member
