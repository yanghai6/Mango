from flask import Blueprint, jsonify
import time

from ..exceptions.exception_auth_error import AuthError

bp = Blueprint("api", __name__)


@bp.route("/time", methods=(["GET"]))
def get_current_time():
    return jsonify({"time": time.time()})


@bp.route("/quarter-mock", methods=(["GET"]))
def get_quarter_mock():
    data = {
        2012: [
            {"quarter": 1, "earnings": 13000},
            {"quarter": 2, "earnings": 16500},
            {"quarter": 3, "earnings": 14250},
            {"quarter": 4, "earnings": 19000},
        ],
        2013: [
            {"quarter": 1, "earnings": 15000},
            {"quarter": 2, "earnings": 12500},
            {"quarter": 3, "earnings": 19500},
            {"quarter": 4, "earnings": 13000},
        ],
        2014: [
            {"quarter": 1, "earnings": 11500},
            {"quarter": 2, "earnings": 13250},
            {"quarter": 3, "earnings": 20000},
            {"quarter": 4, "earnings": 15500},
        ],
        2015: [
            {"quarter": 1, "earnings": 18000},
            {"quarter": 2, "earnings": 13250},
            {"quarter": 3, "earnings": 15000},
            {"quarter": 4, "earnings": 12000},
        ],
    }
    return jsonify(
        {
            "data": data,
            "config": {
                "xAxis": {
                    "tickFormat": ["Quarter 1", "Quarter 2", "Quarter 3", "Quarter 4"],
                    "tickValue": [1, 2, 3, 4],
                }
            },
        }
    )


@bp.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0
