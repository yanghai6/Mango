from app import db
import pandas as pd
from app.backend.models.tables.preferences_raw_data import PreferencesRawData
from app.backend.models.tables.trends_data import TrendsData


def get_trends(category):
    query = TrendsData.query.filter_by(category=category).all()
    result = {}
    for row in query:
        result[row.date] = {"amount": row.amount, "frequency": row.frequency}

    return result


def calculate_delta(result):
    for category in result:
        months = list(map(lambda x: x["date"], result[category]["graphData"]))

        if len(months) < 2:
            result[category]["delta"] = {"amount": 0, "frequency": 0}
            result[category]["percent"] = {"amount": 0, "frequency": 0}
            continue

        months.sort()
        last_month = months[-1]
        second_last_month = months[-2]

        last_amount_index = next(
            (
                index
                for (index, d) in enumerate(result[category]["graphData"])
                if d["date"] == last_month
            ),
            None,
        )
        last_amount = result[category]["graphData"][last_amount_index]["amount"]

        second_last_amount_index = next(
            (
                index
                for (index, d) in enumerate(result[category]["graphData"])
                if d["date"] == second_last_month
            ),
            None,
        )
        second_last_amount = result[category]["graphData"][second_last_amount_index][
            "amount"
        ]

        last_frequency = result[category]["graphData"][last_amount_index]["frequency"]
        second_last_frequency = result[category]["graphData"][second_last_amount_index][
            "frequency"
        ]

        amount_delta = last_amount - second_last_amount
        frequency_delta = last_frequency - second_last_frequency

        amount_percent = amount_delta / second_last_amount * 100
        frequency_percent = frequency_delta / second_last_frequency * 100

        result[category]["delta"] = {
            "amount": amount_delta,
            "frequency": frequency_delta,
        }
        result[category]["percent"] = {
            "amount": amount_percent,
            "frequency": frequency_percent,
        }

    return result


def get_all_trends():
    query = TrendsData.query.all()
    result = {}

    # Populate results with all categories
    for row in query:
        # Noticed that the raw data had NAs for all Financial Transfer amounts, so skipping
        if row.category == "Financial Transfers":
            continue

        if row.category not in result:
            result[row.category] = {}

        if "graphData" not in result[row.category]:
            result[row.category]["graphData"] = []

        result[row.category]["graphData"].append(
            {
                "date": row.date,
                "amount": row.amount,
                "frequency": row.frequency,
            }
        )

    result = calculate_delta(result)

    return result


def process_trends():
    with db.get_engine().connect() as conn:
        raw_data = pd.read_sql(PreferencesRawData.__tablename__, conn)
        raw_data.drop(raw_data.columns[[0, 1, 2, 7, 8]], axis=1, inplace=True)

    # Remove days from the date
    raw_data["date"] = raw_data["date"].apply(lambda x: x.strftime("%Y-%m"))

    # Calculate frequency and amount
    expense = (
        raw_data.groupby(by=["persona_id", "date", "category"])
        .agg(["mean", "count"])
        .reset_index()
    )

    expense.columns = ["persona_id", "date", "category", "amount", "frequency"]

    trends_data = (
        expense.drop(expense.columns[0], axis=1)
        .groupby(["date", "category"])
        .agg({"amount": "mean", "frequency": "mean"})
        .fillna(0)
        .reset_index()
    )

    db.session.bulk_insert_mappings(TrendsData, trends_data.to_dict(orient="records"))

    db.session.commit()
