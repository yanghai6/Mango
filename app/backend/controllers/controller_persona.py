import math
import operator
import random

from app.backend.models.ml.learner.min_offer_learner import predict_min_offer
from app.backend.models.ml.learner.preferences_learner import predict_preferences
from app.backend.models.persona.persona import add_persona
from app.backend.services.service_auth import requires_auth
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from app.constants import PERSONA_MAPPING, CATEGORY_PRODUCT_MAPPING

bp = Blueprint("api/persona", __name__)


@bp.route("/mapping", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_persona_mapping():
    """
    Returns the components that makes up a persona.
    """
    return jsonify(data=PERSONA_MAPPING)


@bp.route("/predict_spending_habit", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def post_predict_spending_habit():
    """
    Returns the predicted spending habit that makes up a persona.
    """
    data = request.json

    age = int(data["age"])
    gender = int(data["gender"])
    marital_status = int(data["marital_status"])
    education = int(data["education"])
    persona_data = [age, gender, marital_status, education]

    result = predict_preferences(persona_data)
    sorted_result = sorted(
        result, key=operator.itemgetter("frequency", "amount"), reverse=True
    )

    income = int(data["income"])
    persona_data = [age, gender, marital_status, education, income]
    interest_value = predict_min_offer(persona_data)
    top_products = calculate_top_5(
        interest_value=interest_value, sorted_category=sorted_result
    )

    description = {
        "age": {"value": age, "description": PERSONA_MAPPING["age"][age]},
        "gender": {"value": gender, "description": PERSONA_MAPPING["gender"][gender]},
        "marital_status": {
            "value": marital_status,
            "description": PERSONA_MAPPING["marital_status"][marital_status],
        },
        "education": {
            "value": education,
            "description": PERSONA_MAPPING["education"][education],
        },
        "income": {"value": income, "description": PERSONA_MAPPING["income"][income]},
    }

    add_persona(persona_data)
    return jsonify(
        data=sorted_result,
        description=description,
        interest=top_products,
        minimum_value=interest_value,
    )


def calculate_top_5(interest_value, sorted_category):

    ## Calculate all products in a category and then sort them by lowest Multiples and Total.
    top_categories = list(map(lambda x: x["category"], sorted_category))
    top_products = list(
        map(lambda category: CATEGORY_PRODUCT_MAPPING[category], top_categories)
    )

    top_5_calculated = []

    for index, products in enumerate(top_products):
        if len(top_5_calculated) < 5:
            sort_product = []
            for product in products:
                if len(top_5_calculated) < 5:
                    multiples_of_product = (
                        0
                        if interest_value / product["value"] < 1
                        else math.ceil(interest_value / product["value"])
                    )
                    if multiples_of_product > 0:
                        sort_product.append(
                            {
                                "title": product["description"],
                                "category": product["category"],
                                "total": product["value"] * multiples_of_product,
                                "multiples": multiples_of_product,
                                "image": product["image"],
                            }
                        )
                else:
                    break
            if sort_product:
                sort_product = sorted(
                    sort_product,
                    key=operator.itemgetter("total", "multiples"),
                    reverse=True,
                )

                top_5_calculated.append(sort_product[0])

        else:
            break

    return top_5_calculated
