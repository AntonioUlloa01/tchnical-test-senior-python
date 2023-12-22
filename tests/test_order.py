import pytest
import json
from app.app import app
from app.services.order_service import OrderService


@pytest.mark.parametrize(
    "date, season_expected",
    [
        ('09-23', 'Fall'),
        ('01-01', 'Winter'),
        ('12-05', 'Winter'),  # Valor correcto 'Fall'
        ('09-24', 'Fall'),
        ('01-30', 'Summer'),  # Valor correcto 'Winter'
        ('05-02', 'Spring'),
        ('04-02', 'Spring'),
        ('10-09', 'Fall')
    ]
)
def test_season_by_date(date, season_expected):
    assert OrderService.get_season(date) == season_expected

# Aun que las pruebas esten fallando la logica es correcta,
# solo que el valor esperado es incorrecto segun la definicion de la tabla


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_season_orders(client):
    response = client.get('/api/order_season')
    assert response.status_code == 200


def test_get_order_by_id(client):
    order_id = 1
    response = client.get(f'/api/order/{order_id}')
    assert response.status_code == 200

    # Caso de prueba donde el id no se encuentra en la base de datos
    order_id = 100
    response = client.get(f'/api/order/{order_id}')
    assert response.status_code == 404


def test_create_order(client):
    # Caso donde la estructura del data no contiene todos los campos requeridos
    data = {'ord_dt': '12/22/2023', 'qt_ordd': 1}
    response = client.post(
        '/api/order',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400

    data = {
        'ord_id': '114-7232801-4607441',
        'ord_dt': '12/22/2023',
        'qt_ordd': 1
    }

    response = client.post(
        '/api/order',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 201


def test_update_order(client):

    # Caso de prueba de actualizacion exitoso
    order_id = 1
    data = {
        'ord_id': '114-7232801-4607448',
        'ord_dt': '12/22/2023',
        'qt_ordd': 1
    }

    response = client.put(
        f'/api/order/{order_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 200

    # Caso de prueba con order no encontrado
    order_id = 999

    response = client.put(
        f'/api/order/{order_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 404

    # Caso de prueba con campos faltantes
    order_id = 1
    data = {
        'ord_id': '114-7232801-4607448',
        'ord_dt': '12/22/2023'
    }

    response = client.put(
        f'/api/order/{order_id}',
        data=json.dumps(data),
        content_type='application/json'
    )
    assert response.status_code == 400


def test_delete_order(client):

    # Caso de prueba de eliminacion exitosa
    order_id = 9

    response = client.delete(f'/api/order/{order_id}')
    assert response.status_code == 200

    # Caso de prueba con order no encontrado
    order_id = 999

    response = client.delete(f'/api/order/{order_id}')
    assert response.status_code == 404
