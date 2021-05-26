from sqlalchemy.sql.sqltypes import String
from recepies.recepie.models.recepie_step import RecepieStep
from recepies.recepie.models.recepie_ingredient import RecepieIngredient
from sqlalchemy import Column, Integer, Text, DateTime, String
from sqlalchemy.orm import relationship
from datetime import datetime
from recepies.database import db

class Recepie(db.Model):
    __tablename__ = 'recepies'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    image = Column(Text)
    summary = Column(Text(120))
    createdAt = Column(DateTime, default=datetime.utcnow)
    ingredients = relationship("RecepieIngredient", uselist=True)
    steps = relationship("RecepieStep", uselist=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Recepie.{self.id} {self.name}>'
    
    @staticmethod
    def from_json(json):
        recepie = Recepie()
        recepie.name = json['name']
        recepie.summary = json['summary']
        recepie.image = json['image']
        recepie.ingredients = [RecepieIngredient(i['id'], i['quantity']) for i in json['ingredients'].values()]
        recepie.steps = [RecepieStep(step, index) for (index, step) in enumerate(json['steps'])]
        return recepie
    
    def to_json(self):
        return {
            "name": self.name,
            "summary": self.summary,
            "image": self.image,
            "link": f'/recepie/{self.id}',
            "steps": [s.step for s in sorted(self.steps, key= lambda s:s.order)],
            "ingredients": [{"name":ri.ingredient.name, "quantity": ri.quantity} for ri in self.ingredients],
            "date": self.createdAt.strftime("%d/%m/%Y %H:%M:%S")
        }
