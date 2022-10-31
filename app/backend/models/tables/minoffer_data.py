from app import db


class MinOfferData(db.Model):
    __tablename__ = "min_offer_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    marital = db.Column(db.Integer, nullable=False)
    education = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Integer, nullable=False)
    min_offer = db.Column(db.Float, nullable=False)
