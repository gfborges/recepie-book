from recepies.database import db
from recepies.recepie.recepie import Recepie

class RecepieRepository:
    def save(self, recepie: Recepie):
        db.session.add(recepie)
        db.commit()

    def get(self, id: int):
        return Recepie.query.get(id)