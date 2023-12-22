from app.database import db


class Order(db.Model):
    __tablename__ = 'order'

    id = db.Column(db.Integer, primary_key=True)
    ord_id = db.Column(db.String(50), nullable=False, unique=True)
    ord_dt = db.Column(db.Date, nullable=False)
    qt_ordd = db.Column(db.Integer, nullable=False)
