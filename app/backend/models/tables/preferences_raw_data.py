from app import db


class PreferencesRawData(db.Model):
    __tablename__ = "preferences_raw_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(120), nullable=False)
    persona_id = db.Column(db.Integer, nullable=False)
    marital = db.Column(db.String(120), nullable=False)
    education = db.Column(db.String(120), nullable=False)
