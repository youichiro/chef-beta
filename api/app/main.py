from fastapi import APIRouter, Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy_future import paginate

from app import models, schemas
from app.dependencies import get_db

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "Hello World!"}


api_router = APIRouter(prefix="/api")


@api_router.get(
    "/projects",
    status_code=200,
    response_model=Page[schemas.Project],
    responses={
        404: {"description": "Not found project"}
    },
)
def get_projects(db: Session = Depends(get_db)):
    query = select(models.Project)
    return paginate(db, query)


app.include_router(api_router)
add_pagination(app)
