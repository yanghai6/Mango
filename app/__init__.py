import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import sentry_sdk
from flask import Flask, render_template
from sentry_sdk.integrations.flask import FlaskIntegration


load_dotenv()


def process_postgres_url():
    uri = os.getenv("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    return uri


def create_app(test_config=None):
    app = Flask(__name__, static_folder="./static")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    if test_config:
        # load the test config if passed in
        app.config.update(test_config)
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = process_postgres_url()
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Configure services
    db.init_app(app)

    # Configure endpoints
    @app.route("/", defaults={"path": ""})
    @app.route("/<path:path>")
    def home(path):
        return render_template("index.html")

    from app.backend.services import service_auth
    from app.backend.controllers import controller_api
    from app.backend.controllers import controller_api_data
    from app.backend.controllers import controller_api_preferences_data
    from app.backend.controllers import controller_api_minoffer_data
    from app.backend.controllers import controller_api_persona_data
    from app.backend.controllers import controller_api_ml
    from app.backend.controllers import controller_persona
    from app.backend.controllers import controller_api_trends

    app.register_blueprint(service_auth.bp, url_prefix="/auth")
    app.register_blueprint(controller_api.bp, url_prefix="/api")
    app.register_blueprint(controller_api_data.bp, url_prefix="/api/data")
    app.register_blueprint(
        controller_api_preferences_data.bp, url_prefix="/api/data/preferences"
    )
    app.register_blueprint(
        controller_api_minoffer_data.bp, url_prefix="/api/data/min_offer"
    )
    app.register_blueprint(
        controller_api_persona_data.bp, url_prefix="/api/data/persona"
    )
    app.register_blueprint(controller_api_ml.bp, url_prefix="/api/ml")
    app.register_blueprint(controller_persona.bp, url_prefix="/api/persona")
    app.register_blueprint(controller_api_trends.bp, url_prefix="/api/trends")

    return app


if os.getenv("SENTRY_URL"):
    sentry_sdk.init(
        dsn=os.getenv("SENTRY_URL"),
        integrations=[FlaskIntegration()],
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,
    )

db = SQLAlchemy()
app = create_app()
