from recepies import db

class Ingredient(db.Model):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    image = db.Column(db.String(64))
    summary = db.Column(db.String(120))

    def __repr__(self):
        return f'<Ingrdient.{self.id} {self.name}>'