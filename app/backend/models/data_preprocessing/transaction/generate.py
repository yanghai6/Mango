import pandas as pd

from sklearn.utils import resample
from app.backend.models.data_preprocessing.utils import *


def load_data(file_name):
    """
    load the original dataset from a bank in Brazil and translate it
    """
    # load the original data.
    raw_df = pd.read_csv(
        file_name,
        encoding="CP1252",
        sep=";",
        decimal=",",
        na_values=" -   ",
        thousands=".",
        parse_dates=[8],
        dayfirst=True,
    )

    # translate columns names
    raw_df.columns = [
        "account",
        "branch_number",
        "city",
        "state",
        "age",
        "gender",
        "total_credit_card_limit",
        "current_available_limit",
        "date",
        "amount",
        "category",
        "purchase_city",
        "purchase_country",
    ]
    df = raw_df[["account", "age", "gender", "date", "amount", "category"]]

    # translate expense categories
    df.replace("HOSP E CLINICA", "Hospital or Clinic", inplace=True)
    df.replace("ARTIGOS ELETRO", "Electronics", inplace=True)
    df.replace("VAREJO", "Convenience Store", inplace=True)
    df.replace("JOALHERIA", "Jewelry", inplace=True)
    df.replace("CIA AEREAS", "Airlines", inplace=True)
    df.replace("HOTEIS", "Hotels", inplace=True)
    df.replace("LOJA DE DEPART", "Department Store", inplace=True)
    df.replace("ALUG DE CARROS", "Car Rent", inplace=True)
    df.replace("INEXISTENTE", "None", inplace=True)
    df.replace("RESTAURANTE", "Restaurant", inplace=True)
    df.replace("POSTO DE GAS", "Gas Station", inplace=True)
    df.replace("VESTUARIO", "Clothing", inplace=True)
    df.replace("MAT CONSTRUCAO", "Construction Material", inplace=True)
    df.replace("TRANS FINANC", "Financial Transfers", inplace=True)
    df.replace("AUTO PE‚AS", "Auto Parts", inplace=True)
    df.replace("M.O.T.O.", "Online Purchases", inplace=True)
    df.replace("SERVI‚O", "Service", inplace=True)
    df.replace("FARMACIAS", "Drugstores", inplace=True)
    df.replace("MOVEIS E DECOR", "Furniture and Decoration", inplace=True)
    df.replace("SUPERMERCADOS", "Supermarket", inplace=True)
    df.replace("SEM RAMO", "Other", inplace=True)
    df.replace("AGENCIA DE TUR", "Tourism Agency", inplace=True)

    return df


def generate_data(df):
    """
    generate more persona info based on the original dataset
    """

    # extract existing accounts
    raw_account = df[["account", "age", "gender"]].drop_duplicates()

    # resample
    account = (
        resample(raw_account, replace=True, n_samples=200, random_state=1)
        .reset_index()
        .drop(columns=["index"])
    )

    # generate marital status
    account["marital"] = ""
    for i in range(len(account)):
        account["marital"][i] = predict_marital(account.age[i], account.gender[i], i)

    # generate education status
    account["education"] = ""
    for i in range(len(account)):
        account["education"][i] = predict_education(
            account.age[i], account.gender[i], i
        )

    # reset personal id
    account = account.reset_index().rename(columns={"index": "id"})

    return account


def generate():
    """
    generate data based on the original dataset from a bank in Brazil
    to mock the data get from banks
    """
    # load original data
    df = load_data("transaction.csv")

    # generate based on original data
    account = generate_data(df)

    # combine generated datasets
    raw_data = pd.merge(df, account, on=["account", "age", "gender"])
    raw_data.drop(columns="account", inplace=True)
    raw_data.sort_values("id", inplace=True)

    # save generated data
    raw_data.to_csv("raw_data.csv", index=False)


if __name__ == "__main__":
    generate()
