from app.backend.models.shared import db
from app import create_app

app = create_app()
app.app_context().push()
db.create_all()
