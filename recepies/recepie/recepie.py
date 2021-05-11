from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from recepies.recepie.recepie_ingredient import RecepieIngredient
from recepies.database import db

class Recepie(db.Model):
    __tablename__ = 'recepies'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    image = Column(String(64))
    summary = Column(String(120))
    createdAt = Column(DateTime, default=datetime.utcnow)
    ingredients = relationship("RecepieIngredient", uselist=True)

    def __repr__(self):
        return f'<Recepie.{self.id} {self.name}>'
