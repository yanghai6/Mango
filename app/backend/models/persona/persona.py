from app import db
from app.backend.models.tables.persona_data import Persona
from sqlalchemy import desc
from datetime import datetime


def add_persona(persona_data):
    existing = Persona.query.filter_by(
        age=persona_data[0],
        gender=persona_data[1],
        marital_status=persona_data[2],
        education=persona_data[3],
        income=persona_data[4],
    ).first()

    if existing is None:
        persona = Persona(
            age=persona_data[0],
            gender=persona_data[1],
            marital_status=persona_data[2],
            education=persona_data[3],
            income=persona_data[4],
            last_accessed=datetime.now(),
        )

        db.session.add(persona)
    else:
        existing.last_accessed = datetime.now()

    db.session.commit()


def get_personas():
    query = Persona.query.order_by(desc(Persona.last_accessed)).all()
    result = []
    for row in query:
        row_data = dict(
            (col, getattr(row, col)) for col in row.__table__.columns.keys()
        )
        result.append(row_data)

    return result
