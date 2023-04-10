from fastapi import APIRouter, Depends, FastAPI
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
    allow_credentials=False,  # cookieをサポートするか
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
    responses={404: {"description": "Not found project"}},
)
def get_projects(db: Session = Depends(get_db)):
    query = select(models.Project)
    return paginate(db, query)


app.include_router(api_router)
add_pagination(app)
