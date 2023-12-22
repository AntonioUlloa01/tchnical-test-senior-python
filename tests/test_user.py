import pytest
from app.services.user_service import create_user


@pytest.mark.parametrize(
    "username, email, expected_result",
    [
        ('juan', 'juan@softtek.com',
         {'message': "Username must be alt least 6 charactears log"}),
        ('juanPablo', None, {'message': "email was not provided"}),
        ('juanPablo', 'example@softtek.com',
         {'message': "Email cannot contain 'example'"}),
        ('juanPablo', 'juanPabloSofttek.com',
         {'message': "Invalid email format"}),
        ('juanPablo', 'juanPablo@@softtek.com',
         {'message': "Invalid email format"})
    ]
)
def test_crete_user(username, email, expected_result):
    assert 'message' in create_user(username, email)


def test_valid_create_user():

    username = 'juanPablo'
    email = 'juanPablo@softtek.com'

    assert 'message'not in create_user(username, email)
