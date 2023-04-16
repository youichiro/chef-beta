from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy_future import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db

app = FastAPI()
allow_origins = ["http://localhost:5173"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def get_root():
    return {"message": "Hello World!"}


api_router = APIRouter(prefix="/api")


@api_router.get(
    "/projects",
    status_code=200,
    response_model=Page[schemas.Project],
)
def get_projects(db: Session = Depends(get_db)):
    query = select(models.Project)
    return paginate(db, query)


@api_router.get(
    "/projects/{project_id}/datasets",
    status_code=200,
    response_model=Page[schemas.Dataset],
)
def get_datasets(project_id: int, db: Session = Depends(get_db)):
    query = select(models.Project).where(models.Project.id == project_id)
    project = db.scalars(query).one_or_none()
    if project is None:
        raise HTTPException(status_code=404, detail=f"Project not found. project_id: {project_id}")

    query = select(models.Dataset).where(models.Dataset.project_id == project_id)
    return paginate(db, query)


@api_router.get(
    "/members",
    status_code=200,
    response_model=Page[schemas.Member],
)
def get_members(db: Session = Depends(get_db)):
    query = select(models.User)
    return paginate(db, query)


app.include_router(api_router)
add_pagination(app)
