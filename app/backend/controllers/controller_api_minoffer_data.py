from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth
import pandas as pd
from app import db, constants
from app.backend.models.data_preprocessing.minoffer.preprocess import (
    preprocess_min_offer,
)
from app.backend.models.tables.minoffer_data import MinOfferData
from app.backend.models.tables.minoffer_raw_data import MinOfferRawData

bp = Blueprint("api/data/min_offer", __name__)


@bp.route("/process", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def process_min_offer_data():
    """
    Processes min offer data.
    """
    csv_file = request.files["file"]
    if csv_file.filename != "":
        raw_data = pd.read_csv(csv_file)
        headers = list(raw_data)

        if headers != constants.RAW_MIN_OFFER_DATA_CSV_HEADERS:
            return "Invalid input file headers", 400

        save_raw_data = raw_data.rename(columns={"id": "persona_id"})
        db.session.bulk_insert_mappings(
            MinOfferRawData, save_raw_data.to_dict(orient="records")
        )

        processed_df = preprocess_min_offer(raw_data)
        db.session.bulk_insert_mappings(
            MinOfferData, processed_df.to_dict(orient="records")
        )

        db.session.commit()

        return "Successfully saved data", 200
    return "No file provided", 400


@bp.route("/clear", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def clear_min_offer_table():
    """
    For testing purposes only. Clears both the min_offer_data table and the min_offer_raw_data table.
    """
    engine = db.get_engine()

    MinOfferData.__table__.drop(engine)
    MinOfferRawData.__table__.drop(engine)

    db.create_all()

    return "Successfully cleared Min Offer data and raw data tables", 200


@bp.route("/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_min_offer_count():
    """
    For testing purposes only. Returns the number of rows in the min_offer_data table
    """
    return jsonify(db.session.query(MinOfferData).count())


@bp.route("/raw/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_min_offer_raw_count():
    """
    For testing purposes only. Returns the number of rows in the min_offer_raw_data table
    """
    return jsonify(db.session.query(MinOfferRawData).count())
