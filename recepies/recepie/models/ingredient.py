from recepies.database import db
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    image = Column(String(64))
    summary = Column(String(120))
    createdAt = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Ingredient.{self.id} {self.name}>'
