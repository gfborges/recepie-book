from recepies import recepie
from injector import inject
from recepies.recepie.services.recepie_repository import RecepieRepository
from recepies.recepie.models import Recepie
from typing import List

class RecepieService():
    @inject
    def __init__(self, recepieRepository: RecepieRepository):
        self.recepieRepository = recepieRepository

    def save(self, json):
        recepie = Recepie.from_json(json)
        return self.recepieRepository.save(recepie)
    
    def delete(self, id:int):
        return self.recepieRepository.delete(id)

    def find_one(self, id) -> Recepie:
        recepie = self.recepieRepository.find_one(id)
        if recepie:
            return recepie.to_json()
    
    def find_many(self, **kwargs) -> List[Recepie]:
        recepies = self.recepieRepository.find_many()
        return [r.to_json() for r in recepies] 



