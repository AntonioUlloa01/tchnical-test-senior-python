from app.models.appointment import Appointment
from app.database import db


class AppointmentService:
    @staticmethod
    def get_all_appointments():
        return Appointment.query.all()

    @staticmethod
    def get_appointment_by_id(appointment_id):
        return Appointment.query.filter(Appointment.id == appointment_id).first()

    @staticmethod
    def create_appointment(date, service, client_id, barber_id):
        new_appointment = Appointment(
            date=date, service=service, client_id=client_id, barber_id=barber_id)
        db.session.add(new_appointment)
        db.session.commit()
        return new_appointment

    @staticmethod
    def update_appointment(appointment_id, new_date, new_service, new_client_id, new_barber_id):
        appointment = Appointment.query.filter(
            Appointment.id == appointment_id).first()
        appointment.date = new_date
        appointment.service = new_service
        appointment.client_id = new_client_id
        appointment.barber_id = new_barber_id
        db.session.commit()
        return appointment

    @staticmethod
    def delete_appointment(appointment_id):
        appointment = Appointment.query.filter(
            Appointment.id == appointment_id).first()
        db.session.delete(appointment)
        db.session.commit()
        return appointment
