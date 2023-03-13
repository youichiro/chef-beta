from pydantic import BaseModel, Field


class Project(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="sample project")
