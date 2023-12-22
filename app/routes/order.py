from flask import Blueprint, jsonify, request, abort
from datetime import datetime
from app.services.order_service import OrderService

order_bp = Blueprint('order', __name__)


@order_bp.route('/order', methods=['GET'])
def get_all_orders():
    orders = OrderService.get_all_orders()
    orders_data = [
        {
            'id': order.id,
            'ord_id': order.ord_id,
            'ord_dt': str(order.ord_dt),
            'qt_ordd': order.qt_ordd
        } for order in orders
    ]

    return jsonify(orders_data)


@order_bp.route('/order/<int:order_id>', methods=['GET'])
def get_order(order_id):

    order = OrderService.get_order_by_id(order_id)

    if order is None:
        abort(404, description='Order not found')

    order_data = {
        'id': order.id,
        'ord_id': order.ord_id,
        'ord_dt': str(order.ord_dt),
        'qt_ordd': order.qt_ordd
    }
    return jsonify(order_data)


@order_bp.route('/order', methods=['POST'])
def create_order():

    data = request.get_json()
    ord_id = data.get('ord_id')
    ord_dt = data.get('ord_dt')
    qt_ordd = data.get('qt_ordd')

    if ord_id is None or ord_dt is None or qt_ordd is None:
        abort(400, description="Missing required fields in the request.")

    new_order = OrderService.create_order(
        ord_id,
        datetime.strptime(ord_dt, '%m/%d/%Y'),
        qt_ordd
    )
    order_data = {'id': new_order.id, 'ord_id': new_order.ord_id,
                  'ord_dt': str(new_order.ord_dt), 'qt_ordd': new_order.qt_ordd}
    return jsonify(order_data), 201


@order_bp.route('/order/<int:order_id>', methods=['PUT'])
def update_order(order_id):

    data = request.get_json()
    new_ord_id = data.get('ord_id')
    new_ord_dt = data.get('ord_dt')
    new_qt_ordd = data.get('qt_ordd')

    existing_order = OrderService.get_order_by_id(order_id)
    if existing_order is None:
        abort(404, description=f"Order with id {order_id} not found.")

    if new_ord_id is None or new_ord_dt is None or new_qt_ordd is None:
        abort(400, description="Missing required fields in the request.")

    updated_order = OrderService.update_order(
        order_id,
        new_ord_id,
        datetime.strptime(new_ord_dt, '%m/%d/%Y'),
        new_qt_ordd
    )
    order_data = {'id': updated_order.id, 'ord_id': updated_order.ord_id,
                  'ord_dt': str(updated_order.ord_dt), 'qt_ordd': updated_order.qt_ordd}
    return jsonify(order_data)


@order_bp.route('/order/<int:order_id>', methods=['DELETE'])
def delete_order(order_id):

    existing_order = OrderService.get_order_by_id(order_id)
    if existing_order is None:
        abort(404, description=f"Order with id {order_id} not found.")

    deleted_order = OrderService.delete_order(order_id)
    order_data = {'id': deleted_order.id, 'ord_id': deleted_order.ord_id,
                  'ord_dt': str(deleted_order.ord_dt), 'qt_ordd': deleted_order.qt_ordd}
    return jsonify(order_data)


@order_bp.route('/order_season', methods=['GET'])
def get_season_orders():
    orders = OrderService.get_all_orders()

    season_orders = [
        {
            'ord_id': order.ord_id,
            'season': OrderService.get_season(order.ord_dt.strftime('%m-%d'))
        } for order in orders
    ]

    return jsonify(season_orders)
