from fastapi import APIRouter, Depends
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy_future import paginate
from sqlalchemy import select
from sqlalchemy.orm import Session

from app import models, schemas
from app.dependencies import get_db


router = APIRouter()

@router.get(
    "/members",
    status_code=200,
    response_model=Page[schemas.Member],
)
def get_members(db: Session = Depends(get_db)):
    query = select(models.User)
    return paginate(db, query)
