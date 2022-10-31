from app import db


class PreferencesData(db.Model):
    __tablename__ = "preferences_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    marital = db.Column(db.Integer, nullable=False)
    education = db.Column(db.Integer, nullable=False)
    category = db.Column(db.Integer, nullable=False)
    frequency = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
