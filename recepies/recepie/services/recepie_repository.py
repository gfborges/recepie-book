from recepies.database import db
from recepies.recepie.models import Recepie

class RecepieRepository:
    def save(self, recepie: Recepie) -> Recepie:
        db.session.add(recepie)
        db.session.commit()
        return recepie

    def delete(self, id:int):
        Recepie.query.filter(Recepie.id == id).delete()

    def find_one(self, id: int) -> Recepie:
        return Recepie.query.get(id)

    def find_many(self, **kwargs):
        return Recepie.query.all()