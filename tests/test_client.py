import pytest
import json
from app.app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_clients(client):
    response = client.get('/api/client')
    assert response.status_code == 200


def test_get_client_by_id(client):
    # Caso donde si existe el cliente con el id buscado
    client_id = 1
    response = client.get(f'/api/client/{client_id}')
    assert response.status_code == 200

    # Caso donde no existe el cliente con el id buscado
    client_id = 999
    response = client.get(f'/api/client/{client_id}')
    assert response.status_code == 404


def test_create_client(client):
    # Caso donde la estructura del data no contiene todos los campos requeridos
    data = {'name': 'Antonio Ulloa'}
    response = client.post(
        '/api/client',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso donde se da de alta un cliente de manera correcta
    data = {'name': 'Antonio Ulloa', 'phone': "444-317-1855"}

    response = client.post(
        '/api/client',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 201


def test_update_client(client):

    # Caso de prueba con campos faltantes
    client_id = 51
    data = {'name': 'Antonio Ulloa'}

    response = client.put(
        f'/api/client/{client_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    # Caso de prueba con cliente no encontrado
    client_id = 999

    response = client.put(
        f'/api/client/{client_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 404

    # Caso de prueba de actualizacion exitoso
    client_id = 51
    data = {'name': 'Antonio Ulloa', 'phone': "444-317-1856"}

    response = client.put(
        f'/api/client/{client_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 200


def test_delete_client(client):

    # Caso de prueba de eliminacion exitosa
    client_id = 51

    response = client.delete(f'/api/client/{client_id}')
    assert response.status_code == 200

    # Caso de prueba con order no encontrado
    client_id = 999

    response = client.delete(f'/api/client/{client_id}')
    assert response.status_code == 404
