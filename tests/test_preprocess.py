import pandas as pd

from app.backend.models.data_preprocessing.transaction.preprocess import (
    preprocess_transaction,
)
from app.backend.models.data_preprocessing.minoffer.preprocess import (
    preprocess_min_offer,
)


def test_preprocess_transaction():
    raw_data = pd.read_csv(
        "app/backend/models/data_preprocessing/transaction/raw_data.csv"
    )

    data = preprocess_transaction(raw_data)

    assert list(data.columns) == [
        "age",
        "gender",
        "marital",
        "education",
        "category",
        "frequency",
        "amount",
    ]
    assert all(data.age) in range(7)
    assert all(data.gender) in range(2)
    assert all(data.marital) in range(5)
    assert all(data.education) in range(3)
    assert all(data.category) in range(22)


def test_preprocess_min_offer():
    raw_data = pd.read_csv(
        "app/backend/models/data_preprocessing/minoffer/raw_data.csv"
    )

    data = preprocess_min_offer(raw_data)

    assert list(data.columns) == [
        "age",
        "gender",
        "marital",
        "education",
        "income",
        "min_offer",
    ]
    assert all(data.age) in range(7)
    assert all(data.gender) in range(2)
    assert all(data.marital) in range(5)
    assert all(data.education) in range(3)
