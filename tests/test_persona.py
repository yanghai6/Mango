from app.backend.models.persona.persona import get_personas, add_persona


def test_personas(app, setup_persona_table):
    with app.app_context():
        personas = get_personas()
        assert len(personas) == 2

        new_persona = [0, 1, 2, 3, 4]
        add_persona(new_persona)

        personas = get_personas()
        assert len(personas) == 3

        existing_persona = [0, 0, 0, 0, 0]
        add_persona(existing_persona)

        personas = get_personas()
        assert len(personas) == 3
