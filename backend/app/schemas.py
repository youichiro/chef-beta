from pydantic import BaseModel, Field

class ProjectType(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="tagging")

    class Config:
        orm_mode = True


class Project(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="sample project")
    project_type: ProjectType

    class Config:
        orm_mode = True


class Guideline(BaseModel):
    id: int = Field(example=1)
    content: str = Field(example="guideline content")

    class Config:
        orm_mode = True


class Member(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="user name")

    class Config:
        orm_mode = True


class Label(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="sample label")
    order: int | None = Field(example=1)
    color: str | None = Field(example="green")

    class Config:
        orm_mode = True


class Document(BaseModel):
    id: int = Field(example=1)
    content: str = Field(example="My name is youichiro ogawa.")

    class Config:
        orm_mode = True


class Dataset(BaseModel):
    id: int = Field(example=1)
    name: str = Field(example="sample dataset")

    class Config:
        orm_mode = True
