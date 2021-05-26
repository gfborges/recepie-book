from flask import Blueprint, render_template, request
from injector import inject
from recepies.recepie import services
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
@router.route("/create", methods=["POST"])
def create(service: RecepieService):
    recepie = request.get_json(force=True)
    return service.save(recepie)

@inject
@router.route("/<int:id>/delete", methods=["POST"])
def delete(id: int, service: RecepieService):
    service.delete(id)
    return "", 200


@inject
@router.route("/<int:id>")
def recepie(id, service: RecepieService):
    ctx = service.find_one(id)
    if ctx != None:
        return render_template("detail.html", context=ctx)
    return f"Recepie {id} not found", 404
