import random


def generar_numero_telefono_aleatorio():
    numero_telefono = "+1-"

    for _ in range(3):
        numero_telefono += str(random.randint(0, 9))

    numero_telefono += "-"

    for _ in range(3):
        numero_telefono += str(random.randint(0, 9))

    numero_telefono += "-"

    for _ in range(4):
        numero_telefono += str(random.randint(0, 9))

    return numero_telefono
