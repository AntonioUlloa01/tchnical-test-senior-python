from flask import Blueprint, jsonify, request, abort
from app.services.barber_service import BarberService


barber_bp = Blueprint('barber', __name__)


@barber_bp.route('/barber', methods=['GET'])
def get_all_barbers():
    barbers = BarberService.get_all_barbers()
    barbers_data = [
        {
            'id': barber.id,
            'name': barber.name,
            'phone': barber.phone
        } for barber in barbers
    ]

    return jsonify(barbers_data)


@barber_bp.route('/barber/<int:barber_id>', methods=['GET'])
def get_barber(barber_id):

    barber = BarberService.get_barber_by_id(barber_id)

    if barber is None:
        abort(404, description='Barber not found')

    barber_data = {
        'id': barber.id,
        'name': barber.name,
        'phone': barber.phone
    }
    return jsonify(barber_data)


@barber_bp.route('/barber', methods=['POST'])
def create_barber():

    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')

    if name is None or phone is None:
        abort(400, description="Missing required fields in the request.")

    new_barber = BarberService.create_barber(name, phone)
    barber_data = {'id': new_barber.id,
                   'name': new_barber.name, 'phone': new_barber.phone}
    return jsonify(barber_data), 201


@barber_bp.route('/barber/<int:barber_id>', methods=['PUT'])
def update_barber(barber_id):

    data = request.get_json()
    new_name = data.get('name')
    new_phone = data.get('phone')

    existing_barber = BarberService.get_barber_by_id(barber_id)
    if existing_barber is None:
        abort(404, description=f"Barber with id {barber_id} not found.")

    if new_name is None or new_phone is None:
        abort(400, description="Missing required fields in the request.")

    updated_barber = BarberService.update_barber(
        barber_id, new_name, new_phone)
    barber_data = {'id': updated_barber.id,
                   'name': updated_barber.name, 'phone': updated_barber.phone}
    return jsonify(barber_data)


@barber_bp.route('/barber/<int:barber_id>', methods=['DELETE'])
def delete_barber(barber_id):

    existing_barber = BarberService.get_barber_by_id(barber_id)
    if existing_barber is None:
        abort(404, description=f"Barber with id {barber_id} not found.")

    deleted_barber = BarberService.delete_barber(barber_id)
    barber_data = {'id': deleted_barber.id,
                   'name': deleted_barber.name, 'phone': deleted_barber.phone}
    return jsonify(barber_data)
