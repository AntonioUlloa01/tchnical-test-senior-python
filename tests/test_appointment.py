import pytest
import json
from app.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_appointment(client):
    response = client.get('/api/appointment')
    assert response.status_code == 200


def test_get_appointment_by_id(client):
    # Caso donde si existe el cliente con el id buscado
    appointment_id = 1
    response = client.get(f'/api/appointment/{appointment_id}')
    assert response.status_code == 200

    # Caso donde no existe el cliente con el id buscado
    appointment_id = 999
    response = client.get(f'/api/appointment/{appointment_id}')
    assert response.status_code == 404


def test_create_appointment(client):
    # Caso donde la estructura del data no contiene todos los campos requeridos
    data = {
        'date': '12/22/2023 09:00',
        'service': 'Haircut',
        'client_id': 1
    }
    response = client.post(
        '/api/appointment',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso donde se da de alta un cliente de manera correcta
    data = {
        'date': '12/22/2023 09:00',
        'service': 'Haircut',
        'client_id': 1,
        'barber_id': 1
    }

    response = client.post(
        '/api/appointment',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 201


def test_update_appointment(client):

    # Caso de prueba con campos faltantes
    appointment_id = 51
    data = {
        'date': '12/22/2023 10:00',
        'service': 'Haircut',
        'client_id': 1
    }

    response = client.put(
        f'/api/appointment/{appointment_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso de prueba con cliente no encontrado
    appointment_id = 999
    data = {
        'date': '12/22/2023 10:00',
        'service': 'Haircut',
        'client_id': 1,
        'barber_id': 1
    }

    response = client.put(
        f'/api/appointment/{appointment_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 404

    # Caso de prueba de actualizacion exitoso
    appointment_id = 51
    data = {
        'date': '12/22/2023 10:00',
        'service': 'Haircut',
        'client_id': 1,
        'barber_id': 1
    }

    response = client.put(
        f'/api/appointment/{appointment_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 200


def test_delete_appointment(client):

    # Caso de prueba de eliminacion exitosa
    appointment_id = 51

    response = client.delete(f'/api/appointment/{appointment_id}')
    assert response.status_code == 200

    # Caso de prueba con order no encontrado
    appointment_id = 999

    response = client.delete(f'/api/appointment/{appointment_id}')
    assert response.status_code == 404


def test_top_5_barbers(client):

    response = client.get('/api/appointment/top5barbers')
    assert response.status_code == 200


def test_top_5_days(client):

    response = client.get('/api/appointment/top5days')
    assert response.status_code == 200
