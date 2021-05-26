from flask import Blueprint, render_template, request, jsonify, redirect, url_for
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
@router.route("/create", methods=["POST"])
def create(service: IngredientService):
    data  = request.get_json(force=True)
    ingredient = service.save(data)
    return jsonify(ingredient.to_json())

@inject
@router.route("/<int:id>/delete", methods=["POST"])
def delete(id: int, service: IngredientService):
    service.delete(id)
    return "", 200

@inject
@router.route("/<int:id>", methods=["GET"])
def ingredient(id, service: IngredientService):
    ctx = service.find_one(id)
    if ctx != None:
        return render_template("detail.html", context=ctx.to_json())
    return f"Ingredient {id} not found", 404


@inject
@router.route("/list", methods=["GET"])
def list_simple(service: IngredientService):
    l = service.find_all_simple()
    return jsonify(l)