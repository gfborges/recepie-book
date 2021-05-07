from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    from recepies.recepie.ingredient import Ingredient
    from recepies.recepie.recepie import Recepie

    db.init_app(app)
    with app.app_context():
        db.create_all()