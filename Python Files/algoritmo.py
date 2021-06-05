import math
from prettytable import PrettyTable as PTable


def f(x):
    return x + 1  # Inserte la función aquí


def hay_cambio_de_signo_en(a, b):
    return (f(a) > 0 > f(b)) or (f(a) < 0 < f(b))


def es_raiz(x):
    return True if (f(x) == 0) else False


def aproximar_raiz_por_iteraciones(a: float, b: float, numero_de_iteraciones: int, metodo: int):
    """
    Algoritmo:

    1. Definir los extremos del intervalo [a_n, b_n].
    2. Revisar si a_n o b_n son raices.
        - Si alguna es raíz, el programa termina.
    3. Revisar si existe cambio de signo en el intervalo [a_n, b_n].
        - Si no hay cambio de signo, el programa termina.
    4. Repetir según el número de iteraciones.
        - Calcular x_n con el método seleccionado (Bisección o Falsa Posición).
        - Calcular el valor de f(x_n).
        - Revisar si f(x_n) es raíz: Si es raíz, terminar el programa, la raíz se encontro.
        - Definir el nuevo intervalo [a_n, b_n]
    5. Imprimir resultados y terminar el programa.
    """
    metodo_op = {
        "Bisección": 0,
        "Falsa Posición": 1
    }

    tabla_resultados = PTable(['n', 'a', 'b', 'x_n', 'f(x_n)'])

    a_n = a
    b_n = b
    x_n = 0.0
    iteraciones = 0

    if (es_raiz(a_n)) or (es_raiz(b_n)):
        if es_raiz(a_n):
            print("\n-----> El extremo del intervalo a_n = ", a_n, " es raíz exacta")
        if es_raiz(b_n):
            print("\n-----> El extremo del intervalo b_n = ", b_n, " es raíz exacta")
        return None

    if (metodo == metodo_op["Bisección"]) or (metodo == metodo_op["Falsa Posición"]):

        if not hay_cambio_de_signo_en(a_n, b_n):
            print("\n---> ERROR: No hay cambio de signo en el intervalo.")
            return None

        while iteraciones < numero_de_iteraciones:

            if metodo == metodo_op["Bisección"]:
                x_n = (a_n + b_n) / 2
            elif metodo == metodo_op["Falsa Posición"]:
                x_n = a_n - (f(a_n) * (b_n - a_n)) / (f(b_n) - f(a_n))
            fx_n = f(x_n)

            tabla_resultados.add_row([iteraciones, a_n, b_n, x_n, fx_n])

            if fx_n == 0:
                break
            else:
                iteraciones += 1

            b_n = x_n if (f(a_n) * fx_n < 0) else b_n
            a_n = x_n if (f(b_n) * fx_n < 0) else a_n

        print(tabla_resultados)
        print("\n-----> La mejor aproximación es x_n = ", x_n, "\n\n")

    else:
        print("\n--->ERROR: No es posible calcular x_n por el método indicado.")


def aproximar_raiz_error_de_truncamiento(_a: int, _b: int, _error_de_truncamiento: float, _metodo: int):
    k = int((math.log((_b - _a) / _error_de_truncamiento) / math.log(2))) + 1
    print("Error de truncamiento: ", _error_de_truncamiento)
    aproximar_raiz_por_iteraciones(_a, _b, k, _metodo)
