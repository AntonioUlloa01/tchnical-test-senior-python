import pytest
import json
from app.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_barbers(client):
    response = client.get('/api/barber')
    assert response.status_code == 200


def test_get_barber_by_id(client):
    # Caso donde si existe el barbero con el id buscado
    barber_id = 1
    response = client.get(f'/api/barber/{barber_id}')
    assert response.status_code == 200

    # Caso donde no existe el barbero con el id buscado
    barber_id = 999
    response = client.get(f'/api/barber/{barber_id}')
    assert response.status_code == 404


def test_create_barber(client):
    # Caso donde la estructura del data no contiene todos los campos requeridos
    data = {'name': 'Ignacio Muriel'}
    response = client.post(
        '/api/barber',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso donde se da de alta un barbero de manera correcta
    data = {'name': 'Ignacio Muriel', 'phone': "444-317-1859"}

    response = client.post(
        '/api/barber',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 201


def test_update_barber(client):

    # Caso de prueba con campos faltantes
    barber_id = 5
    data = {'name': 'Antonio Ulloa'}

    response = client.put(
        f'/api/barber/{barber_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso de prueba con cliente no encontrado
    barber_id = 999

    response = client.put(
        f'/api/barber/{barber_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 404

    # Caso de prueba de actualizacion exitoso
    barber_id = 5
    data = {'name': 'Ignacio Muriel', 'phone': "444-317-1858"}

    response = client.put(
        f'/api/barber/{barber_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 200


def test_delete_barber(client):

    # Caso de prueba de eliminacion exitosa
    barber_id = 5

    response = client.delete(f'/api/barber/{barber_id}')
    assert response.status_code == 200

    # Caso de prueba con order no encontrado
    barber_id = 999

    response = client.delete(f'/api/barber/{barber_id}')
    assert response.status_code == 404
