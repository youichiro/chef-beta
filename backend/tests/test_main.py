from fastapi_pagination import Page

from app import schemas, models
from tests import factories


def test_get_projects(client, db):
    project_type = factories.create_project_type(db)
    project1 = factories.create_project(db, project_type_id=project_type.id, name="dummy project1")
    project2 = factories.create_project(db, project_type_id=project_type.id, name="dummy project2")

    response = client.get("/api/projects")
    assert response.status_code == 200

    page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.Project.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].id == project1.id
    assert items[0].project_type.id == project_type.id
    assert items[1].id == project2.id
    assert items[1].project_type.id == project_type.id


def test_get_members(client, db):
    user1 = factories.create_user(db, name="dummy user1")
    user2 = factories.create_user(db, name="dummy user2")

    response = client.get("/api/members")
    assert response.status_code == 200

    page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.Member.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].id == user1.id
    assert items[1].id == user2.id


def test_get_dataset(client, db):
    project = factories.create_project(db)
    dataset1 = factories.create_dataset(db, project_id=project.id, name="dummy dataset1")
    dataset2 = factories.create_dataset(db, project_id=project.id, name="dummy dataset2")

    project_id = project.id
    response = client.get(f"/api/projects/{project_id}/datasets")
    assert response.status_code == 200

    page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.Dataset.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].id == dataset1.id
    assert items[1].id == dataset2.id
