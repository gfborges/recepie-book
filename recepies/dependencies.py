from injector import singleton
from flask_injector import request

from recepies.recepie.service import RecepieService


def configure(binder):
    binder.bind(RecepieService, to=RecepieService, scope=singleton)