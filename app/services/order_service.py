from app.models.order import Order
from app.database import db


class OrderService:
    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return Order.query.filter(Order.id == order_id).first()

    @staticmethod
    def create_order(ord_id, ord_dt, qt_ordd):
        new_order = Order(ord_id=ord_id, ord_dt=ord_dt, qt_ordd=qt_ordd)
        db.session.add(new_order)
        db.session.commit()
        return new_order

    @staticmethod
    def update_order(order_id, new_ord_id, new_ord_dt, new_qt_ordd):
        order = Order.query.filter(Order.id == order_id).first()
        order.ord_id = new_ord_id
        order.ord_dt = new_ord_dt
        order.qt_ordd = new_qt_ordd
        db.session.commit()
        return order

    @staticmethod
    def delete_order(order_id):
        order = Order.query.filter(Order.id == order_id).first()
        db.session.delete(order)
        db.session.commit()
        return order

    @staticmethod
    def get_season(order_date):

        spring_start = '03-19'
        summer_start = '06-20'
        fall_start = '09-22'
        winter_start = '12-21'

        if spring_start <= order_date < summer_start:
            return 'Spring'
        elif summer_start <= order_date < fall_start:
            return 'Summer'
        elif fall_start <= order_date < winter_start:
            return 'Fall'
        else:
            return 'Winter'
