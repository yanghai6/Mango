import pandas as pd


def aggregate_expense(raw_data):
    """
    aggregate expense info
    """
    raw_expense = raw_data[["id", "date", "amount", "category"]]
    expense = (
        raw_expense.groupby(by=["id", "date", "category"])
        .agg(["count", "mean"])
        .reset_index()
    )
    expense.columns = ["id", "date", "category", "frequency", "amount"]

    return expense


def aggregate_persona(raw_data):
    """
    aggregate persona info
    """
    persona = raw_data[
        ["id", "age", "gender", "marital", "education"]
    ].drop_duplicates()

    return persona


def preprocess_transaction(raw_data):
    """
    take raw data provided by banks and convert it to the format for training
    """

    # convert date to month
    raw_data.date = pd.to_datetime(raw_data.date).dt.strftime("%Y-%m")

    # convert categorical variables to numbers
    for i in range(len(raw_data)):
        if raw_data.loc[i, "age"] is not None:
            raw_data.loc[i, "age"] = int((raw_data.loc[i, "age"] - 20) / 5)

    raw_data.gender = pd.Categorical(raw_data.gender).codes
    raw_data.marital = pd.Categorical(raw_data.marital).codes
    raw_data.education = pd.Categorical(raw_data.education).codes
    raw_data.category = pd.Categorical(raw_data.category).codes

    # aggregate expense and persona info
    expense = aggregate_expense(raw_data)
    persona = aggregate_persona(raw_data)

    # combine aggregated info
    data = pd.merge(persona, expense, on="id")
    data = data.drop(data.columns[[0, 5]], axis=1)
    data = data.fillna(0)

    return data
