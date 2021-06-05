import menu
from algoritmo import aproximar_raiz_error_de_truncamiento
from algoritmo import aproximar_raiz_por_iteraciones
from algoritmo import es_raiz
from algoritmo import hay_cambio_de_signo_en
from utileria import borrar_pantalla
from utileria import capturar_float, capturar_int


def main():
    menu_op = {
        "Bisección": 0,
        "Iteraciones": 0,
        "Truncamiento": 1
    }

    continuar = True
    while continuar:

        borrar_pantalla()
        print("========== APROXIMAR RAICES ==========\n")

        metodo_aprox = menu.capturar_metodo_de_aproximacion()
        metodo_str = "BISECCIÓN" if metodo_aprox == menu_op["Bisección"] else "FALSA POSICIÓN"

        borrar_pantalla()
        a = capturar_float("\nIntroduce el valor de a: ")
        if es_raiz(a):
            print("La raíz es: ", a)
            break

        b = capturar_float("Introduce el valor de b: ")
        if es_raiz(b):
            print("La raíz es: ", b)
            break

        borrar_pantalla()
        if hay_cambio_de_signo_en(a, b):
            tipo_aproximacion = menu.capturar_tipo_de_aproximacion()

            if tipo_aproximacion == menu_op["Iteraciones"]:
                num_iteraciones = menu.capturar_numero_de_iteraciones()
                borrar_pantalla()
                print("========== " + metodo_str + " ==========\n")
                aproximar_raiz_por_iteraciones(a, b, num_iteraciones, metodo_aprox)
            elif tipo_aproximacion == menu_op["Truncamiento"]:
                error_truncamiento = menu.capturar_error_de_truncamiento()
                print("========== " + metodo_str + " ==========\n")
                aproximar_raiz_error_de_truncamiento(a, b, error_truncamiento, metodo_aprox)

        else:
            print("---> ERROR: No hay cambio de signo en el intervalo [", a, ", ", b, "].")

        continuar = bool(capturar_int("\n[0]: Salir.\n[1]: Continuar.\n> Elección: "))


main()
