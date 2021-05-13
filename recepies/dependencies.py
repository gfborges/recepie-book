from injector import singleton

from recepies.recepie.services import RecepieService, IngredientService, FoodService
from recepies.recepie.services.recepie_repository import RecepieRepository
from recepies.recepie.services.ingredient_repository import IngredientRepository

def configure(binder):
    binder.bind(RecepieService, to=RecepieService, scope=singleton)
    binder.bind(RecepieRepository, to=RecepieRepository, scope=singleton)
    binder.bind(IngredientRepository, to=IngredientRepository, scope=singleton)
    binder.bind(IngredientService, to=IngredientService, scope=singleton)
    binder.bind(FoodService, to=FoodService, scope=singleton)