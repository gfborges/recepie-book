from flask import Blueprint, render_template, request
from injector import inject
from recepies.recepie.service import RecepieService
bp = Blueprint("index", __name__)

@inject
@bp.route("/", methods=["GET"])
def home(service: RecepieService):
    ctx = __get_entries(service.get_all)
    return render_template('home.html', context=ctx)

@inject
@bp.route("/recepie", methods=["GET"])
def recepies(service: RecepieService):
    ctx = ctx = __get_entries(service.get_recepies, "recepie")
    ctx["type"] = "recepie"
    return render_template("home.html", context=ctx)

@inject
@bp.route("/recepie/<int:id>")
def recepie(id, service: RecepieService):
    ctx = service.get_recepie(id)
    return render_template("detail.html", context=ctx)

@inject
@bp.route("/ingredient", methods=["GET"])
def ingredients(service: RecepieService):
    ctx = __get_entries(service.get_ingredients, "ingredient")
    return render_template("home.html", context=ctx)

@inject
@bp.route("/ingredient/<int:id>")
def ingredient(id, service: RecepieService):
    ctx = service.get_ingredient(id)
    return render_template("detail.html", context=ctx)

@inject
@bp.route("/search")
def search(service: RecepieService):
    ctx = __get_entries(lambda : service.find_many(request.args.get("query")))
    return render_template("home.html", context=ctx)

def __get_entries(function, _type = None):
    ctx = {}
    ctx["entries"] = function()
    if _type:
        ctx["type"] = _type
    return ctx
