from app import db
from flask import Blueprint, jsonify
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth
from app.backend.models.persona.persona import get_personas
from app.backend.models.tables.persona_data import Persona


bp = Blueprint("api/data/persona", __name__)


@bp.route("/get_all", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_all_personas():
    trends = get_personas()[:4]

    return jsonify(data=trends)


@bp.route("/clear", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def clear_trends_table():
    """
    For testing purposes only. Clears the personas table.
    """
    engine = db.get_engine()

    Persona.__table__.drop(engine)

    db.create_all()

    return "Successfully cleared the personas table", 200


@bp.route("/count", methods=(["GET"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_trends_count():
    """
    For testing purposes only. Returns the number of rows in the personas table
    """
    return jsonify(db.session.query(Persona).count())
