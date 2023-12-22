from flask import Flask
from flask_migrate import Migrate
from .config import Config
from .database import db
from .routes.order import order_bp
from .routes.client import client_bp
from .routes.barber import barber_bp
from .routes.appointment import appointment_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(order_bp, url_prefix='/api')
app.register_blueprint(client_bp, url_prefix='/api')
app.register_blueprint(barber_bp, url_prefix='/api')
app.register_blueprint(appointment_bp, url_prefix='/api')

migrate = Migrate(app, db)

# with app.app_context():
#     db.create_all()


@app.route('/')
def hello():
    return 'Hola, esta es mi API en Flask!'


if __name__ == '__main__':
    app.run(debug=True)
