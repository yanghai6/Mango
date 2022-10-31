from app import constants
from pytorch_lightning.loggers import TensorBoardLogger
import pytorch_lightning as pl


def train(model_type, model_name, max_epochs=10):
    model = model_type()
    logger = TensorBoardLogger(constants.TB_LOGS_DIR, name=model_name)

    trainer = pl.Trainer(max_epochs=max_epochs, logger=logger)

    trainer.fit(model)

    return model
