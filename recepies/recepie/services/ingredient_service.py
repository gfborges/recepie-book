from recepies.recepie.services.ingredient_repository import IngredientRepository
from recepies.recepie.models import Ingredient
from typing import List
from injector import inject

class IngredientService():
    @inject
    def __init__(self, ingredientRepository: IngredientRepository):
        self.ingredientRepository = ingredientRepository

    def find_one(self, id) -> Ingredient:
        return self.ingredientRepository.find_one(id)
    
    def find_many(self, **kwargs) -> List[Ingredient]:
        return self.ingredientRepository.find_many(**kwargs)
