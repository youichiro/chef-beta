from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app import models


app = FastAPI()

@app.get("/")
def get_root():
    return {"message": "Hello World!"}


api_router = APIRouter(prefix="/api")

@api_router.get("/projects")
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()


app.include_router(api_router)
