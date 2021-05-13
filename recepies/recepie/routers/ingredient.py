from flask import Blueprint, render_template, request
from injector import inject
from recepies.recepie import services
from recepies.recepie.services import IngredientService
from recepies.error import NotFound
router = Blueprint("ingredient", __name__, url_prefix="/ingredient")

@inject
@router.route("/", methods=["GET"])
def ingredients(service: IngredientService):
    ctx = {}
    ctx["entries"] = service.find_many()
    ctx["type"] = "ingredient"
    return render_template("home.html", context=ctx)

@inject
@router.route("/<int:id>", methods=["GET"])
def ingredient(id, service: IngredientService):
    ctx = service.find_one(id)
    if ctx != None:
        return render_template("detail.html", context=ctx)
    return f"Ingredient {id} not found"