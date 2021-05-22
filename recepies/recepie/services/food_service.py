from recepies.recepie.models import Ingredient, Recepie
from recepies.recepie.services.ingredient_service import IngredientService
from recepies.recepie.services.recepie_service import RecepieService
from injector import inject
from typing import List, Union

class FoodService():
    @inject
    def __init__(self, recepieService: RecepieService, ingredientService: IngredientService):
        self.recepieService = recepieService
        self.ingredientService = ingredientService
    
    def find_all(self):
        return [
            *self.recepieService.find_many(), 
            *self.ingredientService.find_many()
        ]
    
    def find_many(self, query: str)-> List[Union[Ingredient, Recepie]]:
        return [
            *self.recepieService.find_many(name=query),
            *self.ingredientService.find_many(name=query)
        ]