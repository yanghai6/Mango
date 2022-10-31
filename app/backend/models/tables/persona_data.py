from app import db


class Persona(db.Model):
    __tablename__ = "personas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    marital_status = db.Column(db.Integer, nullable=False)
    education = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Integer, nullable=False)
    last_accessed = db.Column(db.DateTime, nullable=False)
