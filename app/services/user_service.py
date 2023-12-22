import random

# def user(u, e):
#     characters = ['abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789']

#     uuid = ''.join(random.choice(characters) for _ in range(8)) + 'uuid'
#     p = ''.join(random.choice(characters) for _ in range(12))

#     user_data = {
#         'username': u,
#         'password': p,
#         'email': e,
#         'uuid': uuid
#     }

#     if len(user_data['username'] > 5):
#         if len(user_data['password'] > 8):
#             if 'example' not in user_data['email']:
#                 if user_data['email'].count('@') == 1:
#                     if e is not None:
#                         print(f"User created successfully: {user_data}")
#                     else:
#                         print("email was not provided")
#                 else:
#                     print("Invalid email format")
#             else:
#                 print("Email cannot contain 'example'")
#         else:
#             print("Password must be at least 8 characters long")
#     else:
#         print("Username must be alt least 6 charactears log")

# Pasos para refactorizar
# 1. renombramiento de variables y nombre de funcion, las variables al tener nombre acordatos es dificil entender a que hacen referencia,
#    por lo que lo mejor es tener un nombramiento de variables que represente el valor que va a alojar
# 2. definicion de variables como constantes. Como se puede ser el valor de la variable characters no cambia durante la ejecucion  por lo que lo mejor es que pase a ser un contante
#   ademas que al tener una cadena de caracteres dentro de una lista al tener la lista un solo elemento siempre va a tomar el mismo
# 3. validacion de datos definidos para evitar realizar trabajo incesario
# 4. agregar sentencias return para detener el flujo en caso de que una de las condicionales no se cumpla


CHARACTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def create_user(username, email):

    if len(username) <= 5:
        print("Username must be alt least 6 charactears log")
        return {'message': "Username must be alt least 6 charactears log"}

    if email is None:
        print("email was not provided")
        return {'message': "email was not provided"}

    if 'example' in email:
        print("Email cannot contain 'example'")
        return {'message': "Email cannot contain 'example'"}

    if email.count('@') != 1:
        print("Invalid email format")
        return {'message': "Invalid email format"}

    clave = ''.join(random.choice(CHARACTERS) for i in range(12))

    if len(clave) <= 8:
        print("Password must be at least 8 characters long")
        return {'message': "Password must be at least 8 characters long"}

    uuid = ''.join(random.choice(CHARACTERS) for i in range(8)) + 'uuid'

    user_data = {
        'username': username,
        'password': clave,
        'email': email,
        'uuid': uuid
    }

    print(f"User created successfully: {user_data}")
    return user_data
