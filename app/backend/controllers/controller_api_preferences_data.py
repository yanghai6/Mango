from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth
import pandas as pd
from app import db, constants
from app.backend.models.data_preprocessing.transaction.preprocess import (
    preprocess_transaction,
)
from app.backend.models.tables.preferences_data import PreferencesData
from app.backend.models.tables.preferences_raw_data import PreferencesRawData

bp = Blueprint("api/data/preferences", __name__)


@bp.route("/process", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def process_preferences_data():
    """
    Processes preferences data.
    """
    csv_file = request.files["file"]
    if csv_file.filename != "":
        raw_data = pd.read_csv(csv_file)
        headers = list(raw_data)

        if headers != constants.RAW_PREFERENCE_DATA_CSV_HEADERS:
            return "Invalid input file headers", 400

        save_raw_data = raw_data.rename(columns={"id": "persona_id"})
        db.session.bulk_insert_mappings(
            PreferencesRawData, save_raw_data.to_dict(orient="records")
        )

        processed_df = preprocess_transaction(raw_data)
        db.session.bulk_insert_mappings(
            PreferencesData, processed_df.to_dict(orient="records")
        )

        db.session.commit()

        return "Successfully saved data", 200
    return "No file provided", 400


@bp.route("/clear", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def clear_preferences_table():
    """
    For testing purposes only. Clears both the preferences_data table and the preferences_raw_data table.
    """
    engine = db.get_engine()

    PreferencesData.__table__.drop(engine)
    PreferencesRawData.__table__.drop(engine)

    db.create_all()

    return "Successfully cleared Preferences data and raw data tables", 200


@bp.route("/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_preferences_count():
    """
    For testing purposes only. Returns the number of rows in the preferences_data table
    """
    return jsonify(db.session.query(PreferencesData).count())


@bp.route("/raw/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_preferences_raw_count():
    """
    For testing purposes only. Returns the number of rows in the preferences_raw_data table
    """
    return jsonify(db.session.query(PreferencesRawData).count())
