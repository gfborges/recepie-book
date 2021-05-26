from recepies.database import db


class RecepieStep(db.Model):
    __tablename__ = "recepies_steps"
    id = db.Column(db.Integer, primary_key=True)
    id_recepie = db.Column(db.Integer, db.ForeignKey("recepies.id"))
    step = db.Column(db.Text, nullable =False)
    order = db.Column(db.Text, nullable=False) 

    def __init__(self, step: str, order: int):
        self.order = order
        self.step = step