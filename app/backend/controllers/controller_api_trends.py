from app import db
from flask import Blueprint, jsonify
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth
from app.backend.models.trends.trends import process_trends, get_trends, get_all_trends
from app.backend.models.tables.trends_data import TrendsData


bp = Blueprint("api/trends", __name__)


@bp.route("/get/<category>", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_trends_by_category(category):
    trends = get_trends(category)

    return jsonify(trends)


@bp.route("/get_all", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_all():
    all_trends = get_all_trends()

    return jsonify(data=all_trends)


@bp.route("/process", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def process():
    process_trends()

    return "Successfully processed trends data", 200


@bp.route("/clear", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def clear_trends_table():
    """
    For testing purposes only. Clears the trends_data table.
    """
    engine = db.get_engine()

    TrendsData.__table__.drop(engine)

    db.create_all()

    return "Successfully cleared the trends table", 200


@bp.route("/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_trends_count():
    """
    For testing purposes only. Returns the number of rows in the trends_data table
    """
    return jsonify(db.session.query(TrendsData).count())
