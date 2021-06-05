import os


def capturar_float(mensaje: str):
    """
    Permite capturar un número de tipo float imprimiendo un mensaje antes.
    Imprimie un mensaje de error si el valor capturado no pudo ser representado como un número tipo flaot.

    :param mensaje: Texto que será mostrado al pedir el número.
    :return: El número capturado.
    """
    while True:
        try:
            numero = float(input(str(mensaje)))
            return numero
        except ValueError:
            print("\n---> ERROR: El valor introducido no se puede representar como un número real.")


def capturar_int(mensaje: str):
    """
    Permite capturar un número de tipo int imprimiendo un mensaje antes.
    Imprimie un mensaje de error si el valor capturado no pudo ser representado como un número tipo int.

    :param mensaje: Texto que será mostrado al pedir el número.
    :return: El número capturado.
    """
    while True:
        try:
            numero = int(input(str(mensaje)))
            return numero
        except ValueError:
            print("\n---> ERROR: El valor introducido no se puede representar como un número entero.")


def borrar_pantalla():
    """
    Llama a la función `cls` de la consola de windows para limpiar la pantalla.
    """
    __clear()


def diferente_int(x: int, y: int, z: int):
    return (x != y) and (x != z)


def __clear():
    os.system('cls')
