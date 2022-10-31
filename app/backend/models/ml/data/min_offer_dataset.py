import pandas as pd
import torch
from torch.utils.data import Dataset
from app import db
from app.backend.models.tables.minoffer_data import MinOfferData


class MinOfferDataset(Dataset):
    def __init__(self):
        with db.get_engine().connect() as conn:
            self.data = pd.read_sql(MinOfferData.__tablename__, conn)
            self.data.drop(columns=self.data.columns[0], axis=1, inplace=True)
            self.data = pd.get_dummies(
                data=self.data, columns=self.data.columns[[0, 1, 2, 3, 4]]
            )

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        split_at = 1
        input_data = torch.tensor(self.data.iloc[idx, split_at:]).float()
        output_data = torch.tensor(self.data.iloc[idx, :split_at]).float()

        return input_data, output_data
