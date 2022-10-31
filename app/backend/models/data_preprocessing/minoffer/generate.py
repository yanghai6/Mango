import pandas as pd
import numpy as np

from sklearn.utils import resample
from app.backend.models.data_preprocessing.utils import *


def load_data(file_name):
    """
    load the original dataset from a bank in Brazil and translate it
    """
    # load the original data.
    raw_df = pd.read_csv(file_name)

    df = (
        raw_df[["gender", "age", "income"]]
        .dropna()
        .reset_index()
        .drop(columns=["index"])
    )

    return df


def generate_data(df):
    """
    generate more persona info based on the original dataset
    """
    # generate marital status
    df["marital"] = ""
    for i in range(len(df)):
        df["marital"][i] = predict_marital(df.age[i], df.gender[i], i)

    # generate education level
    df["education"] = ""
    for i in range(len(df)):
        df["education"][i] = predict_education(df.age[i], df.gender[i], i)

    # generate minimal offer value
    np.random.seed(0)
    p = np.random.randn(len(df))
    df["min_offer"] = 0
    for i in range(len(df)):
        df["min_offer"][i] = predict_min_offer(df["income"][i], p[i])

    return df


def generate():
    """
    generate data based on the original dataset from a bank in Brazil
    to mock the data get from banks
    """
    # load original data
    df = load_data("minoffer.csv")

    # generate based on original data
    df = generate_data(df)

    # add person id
    raw_data = df.reset_index().rename(columns={"index": "id"})
    raw_data.sort_values("id", inplace=True)

    # save generated data
    raw_data.to_csv("raw_data.csv", index=False)


if __name__ == "__main__":
    generate()
