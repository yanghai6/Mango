import pandas as pd


def preprocess_min_offer(raw_data):
    """
    take raw data provided by banks and convert it to the format for training
    """

    # convert categorical variables to numbers
    for i in range(len(raw_data)):
        if raw_data.loc[i, "age"] is not None:
            raw_data.loc[i, "age"] = int((raw_data.loc[i, "age"] - 20) / 5)
        if raw_data.loc[i, "income"] is not None:
            raw_data.loc[i, "income"] = int(raw_data.loc[i, "income"] / 10000)

    raw_data.gender = pd.Categorical(raw_data.gender).codes
    raw_data.marital = pd.Categorical(raw_data.marital).codes
    raw_data.education = pd.Categorical(raw_data.education).codes

    # sort by id
    raw_data.sort_values("id", inplace=True)

    # formatting
    data = raw_data[["age", "gender", "marital", "education", "income", "min_offer"]]

    return data
