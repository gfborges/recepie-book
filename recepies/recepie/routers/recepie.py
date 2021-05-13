from flask import Blueprint, render_template, request
from injector import inject
from recepies.recepie.services import RecepieService
from recepies.error import NotFound
router = Blueprint("recepie", __name__, url_prefix="/recepie")

@inject
@router.route("/", methods=["GET"])
def recepies(service: RecepieService):
    ctx = {} 
    ctx["entries"] = service.find_many()
    ctx["type"] = "recepie"
    return render_template("home.html", context=ctx)

@inject
@router.route("/<int:id>")
def recepie(id, service: RecepieService):
    ctx = service.get_recepie(id)
    if ctx != None:
        return render_template("detail.html", context=ctx)
    return f"Recepie {id} not found", 404
