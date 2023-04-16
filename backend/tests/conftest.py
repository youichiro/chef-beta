import os

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import main, models
from app.dependencies import get_db


def get_session(worker_id):
    db_user = "root"
    db_password = os.environ["MYSQL_ROOT_PASSWORD"]
    db_host = os.environ["MYSQL_HOST"]
    db_port = os.environ["MYSQL_PORT"]

    db_names = {
        "master": os.environ["MYSQL_TEST_DATABASE"],
        "gw0": os.environ["MYSQL_TEST_DATABASE"],
        "gw1": os.environ["MYSQL_TEST_DATABASE2"],
    }
    db_name = db_names[worker_id]

    sqlalchemy_database_url = f"mysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(sqlalchemy_database_url)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    return session, engine


@pytest.fixture(scope="session")
def app(worker_id):
    db, engine = get_session(worker_id)

    def override_get_db():
        try:
            yield db
        finally:
            db.close()

    main.app.dependency_overrides[get_db] = override_get_db
    models.Base.metadata.create_all(bind=engine)
    yield
    models.Base.metadata.drop_all(bind=engine)


@pytest.fixture(autouse=True)
def init_app(app):
    yield


@pytest.fixture
def db(worker_id):
    db, _ = get_session(worker_id)
    try:
        yield db
        # delete tables
        for table in reversed(models.Base.metadata.sorted_tables):
            db.execute(table.delete())
        db.commit()
    finally:
        db.close()


@pytest.fixture
def client():
    return TestClient(main.app)
