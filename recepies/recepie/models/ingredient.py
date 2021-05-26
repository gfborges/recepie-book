from recepies.database import db
from sqlalchemy import Column, Text, String, Integer, DateTime
from datetime import datetime
from typing import Dict

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), unique=True)
    image = Column(Text)
    summary = Column(String(120))
    createdAt = Column(DateTime, default=datetime.utcnow)

    def __init__(self, name: str, image: str, summary:str):
        self.name = name
        self.image = image
        self.summary = summary

    def __repr__(self):
        return f'<Ingredient.{self.id} {self.name}>'

    def to_json(self):
        return {
            "name": self.name,
            "image": self.image,
            "summary": self.summary,
            "link": f'/ingredient/{self.id}',
            "type": "ingredient",
            "date": self.createdAt.strftime("%d/%m/%Y %H:%M:%S")
        }
    
    def simple(self):
        return {
            "name": self.name,
            "id": self.id,
        }
