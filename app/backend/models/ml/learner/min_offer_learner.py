from app import constants
from app.backend.models.ml.model.min_offer_net import MinOfferNet
import torch


def load_min_offer_model():
    return MinOfferNet.load_from_checkpoint(constants.MIN_OFFER_MODEL_FILE)


def predict_min_offer(persona_data):
    """
    For a single persona, predict the min offer value
    :param persona_data: The persona data (format [age, gender, marital, education, income])
    :return:
    """
    model = load_min_offer_model()
    model.eval()

    persona_tensor = torch.tensor(
        [int(item) for item in persona_data], dtype=torch.float
    )

    prediction = model(persona_tensor)
    result = prediction.cpu().detach().numpy().tolist()

    return result[0]
