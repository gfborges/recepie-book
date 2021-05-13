from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    from recepies.recepie.models import Ingredient, Recepie, RecepieIngredient

    db.init_app(app)
    with app.app_context():
        db.create_all()