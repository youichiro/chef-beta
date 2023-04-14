from fastapi_pagination import Page

from app import schemas


def test_get_projects(client):
    response = client.get("/api/projects")
    assert response.status_code == 200
    assert response.json() == {
        'items': [],
        'total': 0,
        'page': 1,
        'size': 50,
        'pages': 0
    }
