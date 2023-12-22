from app.database import db


class Barber(db.Model):
    __tablename__ = 'barber'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
