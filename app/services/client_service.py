from app.models.client import Client
from app.database import db


class ClientService:
    @staticmethod
    def get_all_clients():
        return Client.query.all()

    @staticmethod
    def get_client_by_id(client_id):
        return Client.query.filter(Client.id == client_id).first()

    @staticmethod
    def create_client(name, phone):
        new_client = Client(name=name, phone=phone)
        db.session.add(new_client)
        db.session.commit()
        return new_client

    @staticmethod
    def update_client(client_id, new_name, new_phone):
        client = Client.query.filter(Client.id == client_id).first()
        client.name = new_name
        client.phone = new_phone
        db.session.commit()
        return client

    @staticmethod
    def delete_client(client_id):
        client = Client.query.filter(Client.id == client_id).first()
        db.session.delete(client)
        db.session.commit()
        return client
