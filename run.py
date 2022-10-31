from app import app
import os


if __name__ == "__main__":
    if os.environ["FLASK_ENV"] != "development":
        app.run()
    else:
        app.run(ssl_context="adhoc")
