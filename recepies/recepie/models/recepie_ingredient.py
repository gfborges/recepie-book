from recepies.database import db
from sqlalchemy.orm import relationship


class RecepieIngredient(db.Model):
    __tablename__ = "recepies_ingredients"
    id_recepie = db.Column(db.Integer, db.ForeignKey("recepies.id"), primary_key=True)
    id_ingredient = db.Column(db.Integer, db.ForeignKey("ingredients.id"), primary_key=True)
    quantity = db.Column(db.Integer)
    ingredient = relationship("Ingredient", uselist=False)

    def __init__(self, id_ingredient:int, quantity: int):
        self.id_ingredient = id_ingredient
        self.quantity = quantity
