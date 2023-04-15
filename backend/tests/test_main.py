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
    assert items[0].id == project1.id
    assert items[0].project_type.id == project_type.id
    assert items[1].id == project2.id
    assert items[1].project_type.id == project_type.id


def test_get_project_detail(client, db):
    project_type = models.ProjectType(name="classification")
    db.add(project_type)
    db.flush()
    project = models.Project(project_type_id=project_type.id, name="demo project")
    db.add(project)
    db.flush()
    guideline = models.Guideline(project_id=project.id, content="demo guideline")
    db.add(guideline)
    dataset1 = models.Dataset(project_id=project.id, name="dataset1")
    dataset2 = models.Dataset(project_id=project.id, name="dataset2")
    db.add_all([dataset1, dataset2])
    db.commit()

    project_id = project.id
    response = client.get(f"/api/projects/{project_id}")
    assert response.status_code == 200

    project_detail = schemas.ProjectDetail.parse_obj(response.json())
    assert project_detail.id == project.id
    assert project_detail.project_type.id == project_type.id
    assert project_detail.guideline.id == guideline.id
    dataset_ids = [dataset.id for dataset in project_detail.datasets]
    assert dataset_ids == [dataset1.id, dataset2.id]


def test_get_members(client, db):
    user1 = models.User(name="user1")
    user2 = models.User(name="user2")
    db.add_all([user1, user2])
    db.commit()

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
