from flask.json import jsonify
from recepies.recepie.services.ingredient_repository import IngredientRepository
from recepies.recepie.models import Ingredient
from typing import List
from injector import inject

class IngredientService():
    @inject
    def __init__(self, ingredientRepository: IngredientRepository):
        self.ingredientRepository = ingredientRepository

    def save(self, json):
        ingredient = Ingredient(json["name"], json["image"], json["summary"])
        return self.ingredientRepository.save(ingredient)
    
    def delete(self, id: int):
        return self.ingredientRepository.delete(id)

    def find_one(self, id) -> Ingredient:
        return self.ingredientRepository.find_one(id)
    
    def find_many(self, **kwargs) -> List[Ingredient]:
        ingredients = self.ingredientRepository.find_many(**kwargs)
        return [i.to_json() for i in ingredients]

    def find_all_simple(self):
        ingredients = self.ingredientRepository.find_many()
        return [i.simple()  for i in ingredients]