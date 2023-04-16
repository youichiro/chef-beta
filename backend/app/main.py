from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from app.members.router import router as members_router
from app.projects.router import router as projects_router

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
api_router.include_router(projects_router)
api_router.include_router(members_router)
app.include_router(api_router)

add_pagination(app)
