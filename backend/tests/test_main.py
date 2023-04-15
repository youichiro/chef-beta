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

    response_data = response.json()
    assert response_data['total'] == 2
    assert response_data['page'] == 1
    assert response_data['size'] == 50
    assert response_data['pages'] == 1

    items = response_data['items']
    assert len(items) == 2
    assert items[0]['name'] == "demo project1"
    assert items[1]['name'] == "demo project2"
