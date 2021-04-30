from recepies.recepie.models import Ingredient

def init_db(app, db):
    db.init_app(app)
    with app.app_context():
        db.create_all()