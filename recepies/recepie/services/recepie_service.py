from recepies.recepie.models.recepie import Recepie
from typing import List
from injector import inject
from recepies.recepie.services.recepie_repository import RecepieRepository
from recepies.recepie.models import Recepie

class RecepieService():
    @inject
    def __init__(self, recepieRepository: RecepieRepository):
        self.recepieRepository = recepieRepository

    def find_one(self, id) -> Recepie:
        return self.recepieRepository.find_one(id)
    
    def find_many(self, **kwargs) -> List[Recepie]:
        return self.recepieRepository.find_many()
