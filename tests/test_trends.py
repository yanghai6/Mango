from app.backend.models.trends.trends import get_trends, get_all_trends, process_trends
from app.backend.models.tables.trends_data import TrendsData


def test_get_trends(app, setup_trends_table):
    with app.app_context():
        result = get_trends("Category1")

    assert result == {
        "2021-12": {"amount": 1.0, "frequency": 1.0},
        "2022-01": {"amount": 2.0, "frequency": 2.0},
    }


def test_get_all_trends(app, setup_trends_table):
    with app.app_context():
        result = get_all_trends()

    assert len(result["Category1"]["graphData"]) == 2
    assert len(result["Category2"]["graphData"]) == 1
    assert len(result["Category3"]["graphData"]) == 1

    assert result["Category1"]["delta"] == {"amount": 1.0, "frequency": 1.0}
    assert result["Category2"]["delta"] == {"amount": 0.0, "frequency": 0.0}


def test_process_trends(app, setup_preferences_raw_data_table):
    with app.app_context():
        process_trends()

        results = TrendsData.query.all()

    assert results[0].amount == 150.0
    assert results[0].frequency == 2
    assert results[0].date == "2021-12"

    assert results[1].amount == 100.0
    assert results[1].frequency == 1
    assert results[1].date == "2022-01"
