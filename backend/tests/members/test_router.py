from fastapi_pagination import Page

from app import schemas
from tests import factories


def test_get_members(client, db):
    user1 = factories.create_user(db, name="dummy user1")
    user2 = factories.create_user(db, name="dummy user2")

    response = client.get("/api/members")
    assert response.status_code == 200

    page: Page = Page.parse_raw(response.content)
    assert page.total == 2
    assert page.page == 1
    assert page.size == 50
    assert page.pages == 1

    items = [schemas.Member.parse_obj(item) for item in page.items]
    assert len(items) == 2
    assert items[0].id == user1.id
    assert items[1].id == user2.id
