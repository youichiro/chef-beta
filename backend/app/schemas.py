from pydantic import BaseModel, Field

class ProjectType(BaseModel):
    name: str = Field(example="tagging")

    class Config:
        orm_mode = True


class Project(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="sample project")
    project_type: ProjectType

    class Config:
        orm_mode = True
