from recepies.recepie import services
from recepies.recepie.services.food_service import FoodService
from recepies.recepie.services import RecepieService
from flask import Blueprint, request, render_template
from injector import inject

router = Blueprint("index", __name__)

@inject
@router.route("/", methods=["GET"])
def home(service: FoodService):
    ctx = {}
    ctx["entries"] = service.find_all()
    return render_template('home.html', context=ctx)

@inject
@router.route("/search")
def search(service: FoodService):
    ctx = {}
    ctx["entries"] = service.find_all()
    return render_template("home.html", context=ctx)
