from recepies.database import db
from recepies.recepie.models import Recepie

class RecepieRepository:
    def save(self, recepie: Recepie):
        db.session.add(recepie)
        db.commit()

    def find_one(self, id: int):
        return Recepie.query.get(id)

    def find_many(self, **kwargs):
        return Recepie.query.all()