from fastapi_pagination import Page

from app import schemas, models


def test_get_projects(client, db):
    project_type = models.ProjectType(name="classification")
    db.add(project_type)
    db.flush()
    project1 = models.Project(project_type_id=project_type.id, name="demo project1")
    project2 = models.Project(project_type_id=project_type.id, name="demo project2")
    db.add_all([project1, project2])
    db.commit()

    response = client.get("/api/projects")
    assert response.status_code == 200

    page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.Project.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].name == 'demo project1'
    assert items[0].project_type.name == 'classification'
    assert items[1].name == 'demo project2'
    assert items[1].project_type.name == 'classification'


def test_get_users(client, db):
    user1 = models.User(name="user1")
    user2 = models.User(name="user2")
    db.add_all([user1, user2])
    db.commit()

    response = client.get("/api/users")
    assert response.status_code == 200

    page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.User.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].name == 'user1'
    assert items[1].name == 'user2'
