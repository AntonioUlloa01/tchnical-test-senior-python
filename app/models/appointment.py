from app.database import db
from datetime import datetime


class Appointment(db.Model):
    __tablename__ = 'appointment'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    service = db.Column(db.String(50), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    barber_id = db.Column(db.Integer, db.ForeignKey(
        'barber.id'), nullable=False)

    client = db.relationship('Client', backref='appointments', lazy=True)
    barber = db.relationship('Barber', backref='appointments', lazy=True)
