from flask import Blueprint, jsonify, request, abort
from app.services.client_service import ClientService

client_bp = Blueprint('client', __name__)


@client_bp.route('client', methods=['GET'])
def get_all_clients():
    clients = ClientService.get_all_clients()
    clients_data = [
        {
            'id': client.id,
            'name': client.name,
            'phone': client.phone
        } for client in clients
    ]

    return jsonify(clients_data)


@client_bp.route('client/<int:client_id>', methods=['GET'])
def get_client(client_id):

    client = ClientService.get_client_by_id(client_id)

    if client is None:
        abort(404, description='Client not found')

    client_data = {
        'id': client.id,
        'name': client.name,
        'phone': client.phone
    }
    return jsonify(client_data)


@client_bp.route('client', methods=['POST'])
def create_client():

    data = request.get_json()
    name = data.get('name')
    phone = data.get('phone')

    if name is None or phone is None:
        abort(400, description="Missing required fields in the request.")

    new_client = ClientService.create_client(name, phone)

    client_data = {'id': new_client.id,
                   'name': new_client.name,
                   'phone': new_client.phone
                   }
    return jsonify(client_data), 201


@client_bp.route('client/<int:client_id>', methods=['PUT'])
def update_client(client_id):

    data = request.get_json()
    new_name = data.get('name')
    new_phone = data.get('phone')

    existing_client = ClientService.get_client_by_id(client_id)
    if existing_client is None:
        abort(404, description=f"Client with id {client_id} not found.")

    if new_name is None or new_phone is None:
        abort(400, description="Missing required fields in the request.")

    updated_client = ClientService.update_client(
        client_id, new_name, new_phone)
    client_data = {'id': updated_client.id,
                   'name': updated_client.name, 'phone': updated_client.phone}
    return jsonify(client_data)


@client_bp.route('client/<int:client_id>', methods=['DELETE'])
def delete_client(client_id):

    existing_client = ClientService.get_client_by_id(client_id)
    if existing_client is None:
        abort(404, description=f"Client with id {client_id} not found.")

    deleted_client = ClientService.delete_client(client_id)
    client_data = {'id': deleted_client.id,
                   'name': deleted_client.name, 'phone': deleted_client.phone}
    return jsonify(client_data)
