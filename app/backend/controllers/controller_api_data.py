from app import db
from flask import Blueprint
from flask_cors import cross_origin
from app.backend.services.service_auth import requires_auth

bp = Blueprint("api/data", __name__)


@bp.route("/create_all", methods=(["POST"]))
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def create_all():
    """
    Endpoint to create all database tables defined by db schemas
    """
    db.create_all()

    return "Successfully create all database tables", 200
