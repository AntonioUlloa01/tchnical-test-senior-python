from flask import Blueprint, jsonify, request, abort
from sqlalchemy import func
from datetime import datetime
from app.services.appointment_service import AppointmentService
from app.models.barber import Barber
from app.models.appointment import Appointment
from app.database import db

appointment_bp = Blueprint('appointment', __name__)


@appointment_bp.route('/appointment', methods=['GET'])
def get_all_appointments():
    appointments = AppointmentService.get_all_appointments()
    appointments_data = [
        {
            'id': appointment.id,
            'date': str(appointment.date),
            'service': appointment.service,
            'client_id': appointment.client_id,
            'barber_id': appointment.barber_id
        } for appointment in appointments
    ]

    return jsonify(appointments_data)


@appointment_bp.route('/appointment/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):

    appointment = AppointmentService.get_appointment_by_id(appointment_id)

    if appointment is None:
        abort(404, description='Appointment not found')

    appointment_data = {
        'id': appointment.id,
        'date': str(appointment.date),
        'service': appointment.service,
        'client_id': appointment.client_id,
        'barber_id': appointment.barber_id
    }
    return jsonify(appointment_data)


@appointment_bp.route('/appointment', methods=['POST'])
def create_appointment():

    data = request.get_json()
    date = data.get('date')
    service = data.get('service')
    client_id = data.get('client_id')
    barber_id = data.get('barber_id')

    if date is None or service is None or client_id is None or barber_id is None:
        abort(400, description="Missing required fields in the request.")

    new_appointment = AppointmentService.create_appointment(
        datetime.strptime(date, '%m/%d/%Y %H:%M'),
        service,
        client_id,
        barber_id
    )
    appointment_data = {
        'id': new_appointment.id,
        'date': str(new_appointment.date),
        'service': new_appointment.service,
        'client_id': new_appointment.client_id,
        'barber_id': new_appointment.barber_id
    }
    return jsonify(appointment_data), 201


@appointment_bp.route('/appointment/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):

    data = request.get_json()
    new_date = data.get('date')
    new_service = data.get('service')
    new_client_id = data.get('client_id')
    new_barber_id = data.get('barber_id')

    existing_appointment = AppointmentService.get_appointment_by_id(
        appointment_id)
    if existing_appointment is None:
        abort(404, description=f"Appointment with id {
              appointment_id} not found.")

    if new_date is None or new_service is None or new_client_id is None or new_barber_id is None:
        abort(400, description="Missing required fields in the request.")

    updated_appointment = AppointmentService.update_appointment(
        appointment_id,
        datetime.strptime(new_date, '%m/%d/%Y %H:%M'),
        new_service,
        new_client_id,
        new_barber_id
    )
    appointment_data = {'id': updated_appointment.id, 'date': str(updated_appointment.date), 'service': updated_appointment.service,
                        'client_id': updated_appointment.client_id, 'barber_id': updated_appointment.barber_id}
    return jsonify(appointment_data)


@appointment_bp.route('/appointment/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):

    existing_appointment = AppointmentService.get_appointment_by_id(
        appointment_id)
    if existing_appointment is None:
        abort(404, description=f"Appointment with id {
              appointment_id} not found.")

    deleted_appointment = AppointmentService.delete_appointment(appointment_id)
    appointment_data = {'id': deleted_appointment.id, 'date': str(deleted_appointment.date), 'service': deleted_appointment.service,
                        'client_id': deleted_appointment.client_id, 'barber_id': deleted_appointment.barber_id}
    return jsonify(appointment_data)


@appointment_bp.route('/appointment/top5barbers', methods=['GET'])
def top_5_barbers():

    barbers_with_appointments = db.session.query(
        Barber.id,
        Barber.name,
        Barber.phone,
        func.count(Appointment.id).label('appointments')
    ).join(
        Appointment
    ).group_by(
        Barber.id
    ).order_by(
        func.count(Appointment.id).desc()
    ).limit(5).all()

    # Formatear los resultados con posición
    top_5_barbers_data = [
        {
            'No': i + 1,
            'phone_number': barber.phone,
            'name': barber.name,
            'appointments': barber.appointments
        } for i, barber in enumerate(barbers_with_appointments)
    ]

    return jsonify(top_5_barbers_data)


@appointment_bp.route('/appointment/countByDay',  methods=['GET'])
def count_by_day():

    appointments_count_by_day = db.session.query(
        func.strftime('%m/%d/%Y', Appointment.date).label('date'),
        func.count(Appointment.id).label('num_appointments')
    ).group_by(
        func.strftime('%m/%d/%Y', Appointment.date)
    ).order_by(
        func.count(Appointment.id).desc()
    ).all()

    appointments_count_by_day_data = [
        {
            'date': day.date,
            'num_appointments': day.num_appointments
        } for day in appointments_count_by_day
    ]

    return jsonify(appointments_count_by_day_data)


@appointment_bp.route('/appointment/top5days', methods=['GET'])
def top_5_days():

    days_of_the_week = {
        "0": "Sunday",
        "1": "Monday",
        "2": "Tuesday",
        "3": "Wednesday",
        "4": "Thursday",
        "5": "Friday",
        "6": "Saturday",
    }

    top_5_days_data = db.session.query(
        func.strftime('%m/%d/%Y', Appointment.date).label('date'),
        func.strftime('%w', Appointment.date).label('day_of_week'),
        func.count(Appointment.id).label('num_appointments')
    ).group_by(
        func.strftime('%m/%d/%Y', Appointment.date)
    ).order_by(
        func.count(Appointment.id).desc()
    ).limit(5).all()

    top_5_days_result = []

    for top_day in top_5_days_data:

        top_barber = db.session.query(
            func.count(Appointment.id).label('count_by_day'),
            Appointment.date,
            Barber.name.label('barber_with_more_appointments')
        ).join(
            Barber,
            Appointment.barber_id == Barber.id
        ).filter(
            func.strftime('%m/%d/%Y', Appointment.date) == top_day.date
        ).group_by(
            Appointment.barber_id
        ).order_by(
            func.count(Appointment.id).desc()
        ).limit(1).all()

        # Formatear los resultados
        top_5_days_result.append(
            {
                'date': top_day.date,
                'day_of_week': days_of_the_week[top_day.day_of_week],
                'num_appointments': top_day.num_appointments,
                'barber_with_more_appointments': top_barber[0].barber_with_more_appointments
            }
        )

    return jsonify(top_5_days_result)
