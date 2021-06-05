import utileria as util


def capturar_metodo_de_aproximacion():
    """ :return: 0: Bisección | 1: Falsa posición """
    metodo_biseccion = 0
    metodo_falsa_posicion = 1

    print("> Selecciona el método de aproximación:\n")
    print("[0] Bisección.")
    print("[1] Falsa posición.")

    eleccion_usuario = -1
    while (eleccion_usuario != metodo_biseccion) and (eleccion_usuario != metodo_falsa_posicion):
        eleccion_usuario = util.capturar_int("> Elección: ")

        if (eleccion_usuario != metodo_biseccion) and (eleccion_usuario != metodo_falsa_posicion):
            print("\n---> ERROR: El valor no corresponde con ninguna opción.\n")

    return eleccion_usuario


def capturar_tipo_de_aproximacion():
    """ :return: 0: Iteraciones | 1: Truncamiento """
    op_iteraciones = 0
    op_error_de_truncamiento = 1

    print("> Seleccione el tipo de aproximación:")
    print("[0] Aproximar por iteraciones.")
    print("[1] Aproximar por truncamiento.")

    eleccion_usuario = -1

    while util.diferente_int(eleccion_usuario, op_iteraciones, op_error_de_truncamiento):
        eleccion_usuario = util.capturar_int("> Elección: ")

        if util.diferente_int(eleccion_usuario, op_iteraciones, op_error_de_truncamiento):
            print("\n---> ERROR: El valor no corresponde con ninguna opción.\n")

    return eleccion_usuario


def capturar_numero_de_iteraciones():
    numero_de_iteraciones = 0
    while numero_de_iteraciones <= 0:
        numero_de_iteraciones = util.capturar_int("\nIntroduce el número de iteraciones: ")

        if numero_de_iteraciones <= 0:
            print("\n---> ERROR: El número de iteraciones no puede ser menor o igual a cero.\n")

    return numero_de_iteraciones


def capturar_error_de_truncamiento():
    error_de_truncamiento = 0.0

    while error_de_truncamiento <= 0:
        error_de_truncamiento = util.capturar_float("\nIntroduce el error de truncamiento: ")

        if error_de_truncamiento <= 0:
            print("\n---> ERROR: El error de truncamiento no puede ser menor o igual a cero.\n")

    return error_de_truncamiento
