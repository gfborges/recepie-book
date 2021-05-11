from injector import singleton
from flask_injector import request

from recepies.recepie.service import RecepieService
from recepies.recepie.recepie_repository import RecepieRepository


def configure(binder):
    binder.bind(RecepieService, to=RecepieService, scope=singleton)
    binder.bind(RecepieRepository, to=RecepieRepository, scope=singleton)