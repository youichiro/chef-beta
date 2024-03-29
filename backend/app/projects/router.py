from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy_future import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db

router = APIRouter()


@router.get(
    "/projects",
    status_code=200,
    response_model=Page[schemas.Project],
)
def get_projects(db: Session = Depends(get_db)):
    query = select(models.Project)
    return paginate(db, query)


@router.get(
    "/projects/{project_id}",
    status_code=200,
    response_model=schemas.Project,
    responses={
        404: {"description": "Project not found"},
    },
)
def get_project(project_id: int, db: Session = Depends(get_db)):
    query = select(models.Project).where(models.Project.id == project_id)
    project = db.scalars(query).one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail=f"Project not found. project_id: {project_id}")
    return project


@router.get(
    "/projects/{project_id}/guideline",
    status_code=200,
    response_model=schemas.Guideline | None,
    responses={
        404: {"description": "Project not found"},
    },
)
def get_guideline(project_id: int, db: Session = Depends(get_db)):
    query = select(models.Project).where(models.Project.id == project_id)
    project = db.scalars(query).one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail=f"Project not found. project_id: {project_id}")
    return project.guideline


@router.get(
    "/projects/{project_id}/datasets",
    status_code=200,
    response_model=Page[schemas.Dataset],
    responses={
        404: {"description": "Project not found"},
    },
)
def get_datasets(project_id: int, db: Session = Depends(get_db)):
    query = select(models.Project).where(models.Project.id == project_id)
    project = db.scalars(query).one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail=f"Project not found. project_id: {project_id}")
    query = select(models.Dataset).where(models.Dataset.project_id == project_id)
    return paginate(db, query)


@router.get(
    "/projects/{project_id}/members",
    status_code=200,
    response_model=Page[schemas.ProjectMember],
    responses={
        404: {"description": "Project not found"},
    },
)
def get_project_members(project_id: int, db: Session = Depends(get_db)):
    query = select(models.Project).where(models.Project.id == project_id)
    project = db.scalars(query).one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail=f"Project not found. project_id: {project_id}")
    query = select(models.ProjectMember).where(models.ProjectMember.project_id == project_id)
    return paginate(db, query)
