import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi.testclient import TestClient

from app import main, models
from app.dependencies import get_db


db_user = "root"
db_password = os.environ["MYSQL_ROOT_PASSWORD"]
db_host = os.environ["MYSQL_HOST"]
db_port = os.environ["MYSQL_PORT"]
db_name = os.environ["MYSQL_TEST_DATABASE"]
sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
engine = create_engine(sqlalchemy_database_url)


def override_get_db():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@pytest.fixture(scope="session")
def app():
    main.app.dependency_overrides[get_db] = override_get_db
    models.Base.metadata.create_all(bind=engine)
    yield main.app
    models.Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def init_app(app):
    yield


@pytest.fixture
def client(app):
    return TestClient(app)
