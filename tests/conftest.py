import pytest
from app import create_app, db
from app.backend.models.tables.trends_data import TrendsData
from app.backend.models.tables.persona_data import Persona
from app.backend.models.tables.preferences_raw_data import PreferencesRawData
from datetime import date, datetime


@pytest.fixture
def app():
    config = {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://"}

    app = create_app(config)

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


@pytest.fixture
def setup_trends_table(app):
    trends = [
        TrendsData(date="2021-12", category="Category1", frequency=1, amount=1),
        TrendsData(date="2022-01", category="Category1", frequency=2, amount=2),
        TrendsData(date="2021-12", category="Category2", frequency=1, amount=1),
        TrendsData(date="2022-01", category="Category3", frequency=2, amount=2),
    ]

    commit_all_to_db(app, trends)


@pytest.fixture
def setup_preferences_raw_data_table(app):
    date1 = date.fromisoformat("2021-12-01")
    date2 = date.fromisoformat("2022-01-01")

    data = [
        PreferencesRawData(
            age=1,
            gender="male",
            date=date1,
            amount=100,
            category="Category1",
            persona_id=0,
            marital="Marital",
            education="Education",
        ),
        PreferencesRawData(
            age=1,
            gender="male",
            date=date1,
            amount=200,
            category="Category1",
            persona_id=0,
            marital="Marital",
            education="Education",
        ),
        PreferencesRawData(
            age=1,
            gender="male",
            date=date2,
            amount=100,
            category="Category1",
            persona_id=1,
            marital="Marital",
            education="Education",
        ),
    ]

    commit_all_to_db(app, data)


@pytest.fixture
def setup_persona_table(app):
    date1 = datetime.fromisoformat("2021-12-01")
    personas = [
        Persona(
            age=0,
            gender=0,
            marital_status=0,
            education=0,
            income=0,
            last_accessed=date1,
        ),
        Persona(
            age=1,
            gender=1,
            marital_status=1,
            education=1,
            income=1,
            last_accessed=date1,
        ),
    ]

    commit_all_to_db(app, personas)


def commit_all_to_db(app, data):
    with app.app_context():
        for item in data:
            db.session.add(item)

        db.session.commit()
