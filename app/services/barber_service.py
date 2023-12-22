from app.models.barber import Barber
from app.database import db


class BarberService:
    @staticmethod
    def get_all_barbers():
        return Barber.query.all()

    @staticmethod
    def get_barber_by_id(barber_id):
        return Barber.query.filter(Barber.id == barber_id).first()

    @staticmethod
    def create_barber(name, phone):
        new_barber = Barber(name=name, phone=phone)
        db.session.add(new_barber)
        db.session.commit()
        return new_barber

    @staticmethod
    def update_barber(barber_id, new_name, new_phone):
        barber = Barber.query.filter(Barber.id == barber_id).first()
        barber.name = new_name
        barber.phone = new_phone
        db.session.commit()
        return barber

    @staticmethod
    def delete_barber(barber_id):
        barber = Barber.query.filter(Barber.id == barber_id).first()
        db.session.delete(barber)
        db.session.commit()
        return barber
