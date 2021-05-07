from recepies.database import db

class RecepieIngredient(db.Model):
    __tablename__ = "recepies_ingredients"
    id_recepie = db.Column(db.Integer, db.ForeignKey("recepies.id"), primary_key=True)
    id_ingredient = db.Column(db.Integer, db.ForeignKey("ingredients.id"), primary_key=True)
    quantity = db.Column(db.Integer)
