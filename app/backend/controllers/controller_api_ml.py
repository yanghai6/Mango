from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth
from app.backend.models.ml.learner.trainer import train
from app.backend.models.ml.learner.preferences_learner import predict_preferences
from app.backend.models.ml.learner.min_offer_learner import predict_min_offer
from app.backend.models.ml.model.preference_net import PreferenceNet
from app.backend.models.ml.model.min_offer_net import MinOfferNet
from app import constants
import os
import shutil


bp = Blueprint("api/ml", __name__)


@bp.route("/preferences/predict", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def preferences_predict():
    """
    Predicts the preferences for a given persona
    """
    data = request.form
    age = int(data["age"])
    gender = int(data["gender"])
    marital_status = int(data["marital_status"])
    education = int(data["education"])
    persona_data = [age, gender, marital_status, education]

    result = predict_preferences(persona_data)
    return jsonify(result)


@bp.route("/preferences/train", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def train_preferences():
    """
    Endpoint to train the Preferences model and update the current working model
    """
    model_name = "preferences"
    train(PreferenceNet, model_name, max_epochs=10)

    copy_ckpt_file(model_name, constants.PREFERENCES_MODEL_FILE)

    return "Trained successfully", 200


@bp.route("/min_offer/predict", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def min_offer_predict():
    """
    Predicts the min offer for a given persona
    """
    data = request.form
    age = int(data["age"])
    gender = int(data["gender"])
    marital_status = int(data["marital_status"])
    education = int(data["education"])
    income = int(data["income"])
    persona_data = [age, gender, marital_status, education, income]

    result = predict_min_offer(persona_data)
    return jsonify(result)


@bp.route("/min_offer/train", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def train_min_offer():
    """
    Endpoint to train the Min Offer model and update the current working model
    """
    model_name = "min_offer"
    train(MinOfferNet, model_name, max_epochs=10)

    copy_ckpt_file(model_name, constants.MIN_OFFER_MODEL_FILE)

    return "Trained successfully", 200


def copy_ckpt_file(model_name, dst):
    logs_dir = os.path.join(constants.TB_LOGS_DIR, model_name)
    versions = os.listdir(logs_dir)
    versions.sort()
    latest_version = str(versions[-1])

    checkpoints_dir = os.path.join(logs_dir, latest_version, "checkpoints")
    checkpoints_file = os.listdir(checkpoints_dir)[0]
    shutil.copyfile(
        os.path.join(checkpoints_dir, checkpoints_file),
        dst,
    )
