from app import db


class TrendsData(db.Model):
    __tablename__ = "trends_data"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(10), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    frequency = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Float, nullable=False)
