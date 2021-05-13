from recepies.database import db
from recepies.recepie.models import Ingredient
from typing import List

class IngredientRepository():
    def save(self, ingredient: Ingredient)-> Ingredient:
        db.session.add(ingredient)
        db.session.commit(ingredient)
        return ingredient
    
    def find_one(self, id: int) -> List[Ingredient]:
        return Ingredient.query.get(id)
    
    def find_many(self, **kwargs):
        return Ingredient.query.all()