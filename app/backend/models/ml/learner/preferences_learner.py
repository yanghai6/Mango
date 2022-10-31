from app import constants
from app.backend.models.ml.model.preference_net import PreferenceNet

from pytorch_lightning.loggers import TensorBoardLogger
import numpy as np
import pytorch_lightning as pl

import torch


def load_preferences_model():
    return PreferenceNet.load_from_checkpoint(constants.PREFERENCES_MODEL_FILE)


def train(model_type, model_name, max_epochs=10):
    model = model_type()
    logger = TensorBoardLogger(constants.TB_LOGS_DIR, name=model_name)

    trainer = pl.Trainer(max_epochs=max_epochs, logger=logger)

    trainer.fit(model)

    return model


def convert_one_hot(persona_data):
    """
    For a single persona, convert into one-hot encoding for each category.
    :param persona_data: a list [age, gender, marital, education]
    :return: a numpy array the one-hot codes for each category
    """
    # convert persona data to one-hot encoding
    age = np.eye(len(constants.AGE))[persona_data[0]]
    gender = np.eye(len(constants.GENDER))[persona_data[1]]
    marital = np.eye(len(constants.MARITAL))[persona_data[2]]
    education = np.eye(len(constants.EDUCATION))[persona_data[3]]
    persona = np.concatenate((age, gender, marital, education))

    # convert each category to one-hot encoding
    category = np.eye(len(constants.CATEGORIES))

    # concatenate one-hot codes for persona and category
    stacked_persona = np.stack((persona for i in range(len(constants.CATEGORIES))))
    return np.concatenate((stacked_persona, category), axis=1)


def predict_preferences(persona_data):
    """
    For a single persona, predict the frequency and amount for each category.
    :param persona_data: The persona data (format [age, gender, marital, education])
    :return:
    """
    model = load_preferences_model()
    model.eval()

    one_hot_data = torch.from_numpy(convert_one_hot(persona_data))

    prediction = model(one_hot_data)
    result = prediction.cpu().detach().numpy()
    result = np.abs(result)
    result[result[:, 0] > 10] = 0

    ret = []
    for i, (frequency, amount) in enumerate(result.tolist()):
        ret.append(
            {
                "category": constants.CATEGORIES[i],
                "frequency": frequency,
                "amount": amount,
            }
        )

    return ret
