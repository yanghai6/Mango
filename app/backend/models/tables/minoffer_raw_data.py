from app import db


class MinOfferRawData(db.Model):
    __tablename__ = "min_offer_raw_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    persona_id = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Integer, nullable=False)
    marital = db.Column(db.String(120), nullable=False)
    education = db.Column(db.String(120), nullable=False)
    min_offer = db.Column(db.Float, nullable=False)
