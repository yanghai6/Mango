import torch
import torch.nn as nn
from pytorch_lightning.utilities.types import EVAL_DATALOADERS
from torch.nn import functional as F
import pytorch_lightning as pl
from app.backend.models.ml.data.data_loader import get_data_loader
from app.backend.models.ml.data.min_offer_dataset import MinOfferDataset


class MinOfferNet(pl.LightningModule):
    def __init__(self):
        super().__init__()
        # Set up DataLoaders
        self.train_loader = None
        self.val_loader = None

        # Model params
        self.linear1 = nn.Linear(5, 10)
        self.linear2 = nn.Linear(10, 20)
        self.linear3 = nn.Linear(20, 1)

    def load_data(self):
        self.train_loader, self.val_loader = get_data_loader(MinOfferDataset())

    def forward(self, x):
        x = x.type(torch.FloatTensor)
        x = self.linear1(x)
        x = F.relu(x)
        x = self.linear2(x)
        x = F.relu(x)
        x = self.linear3(x)
        return x

    def training_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.mse_loss(y_hat, y)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        y_hat = self.forward(x)
        loss = F.mse_loss(y_hat, y)
        self.log("val_loss", loss)
        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=0.02)
        return optimizer

    def train_dataloader(self) -> EVAL_DATALOADERS:
        if self.train_loader is None:
            self.load_data()

        return self.train_loader

    def test_dataloader(self) -> EVAL_DATALOADERS:
        if self.val_loader is None:
            self.load_data()

        return self.val_loader

    def val_dataloader(self) -> EVAL_DATALOADERS:
        if self.val_loader is None:
            self.load_data()

        return self.val_loader

    def predict_dataloader(self) -> EVAL_DATALOADERS:
        if self.val_loader is None:
            self.load_data()

        return self.val_loader
