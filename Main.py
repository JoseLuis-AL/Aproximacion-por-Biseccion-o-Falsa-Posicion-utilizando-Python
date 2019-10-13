from Algoritmo import EsRaiz
from Algoritmo import HayCambioDeSignoEn
from Algoritmo import AproximarRaizPorIteraciones
from Algoritmo import AproximarRaizErrorDeTruncamiento
from Algoritmo import MetodosDeAproximacion

from Utileria import CapturarNumeroReal
from Utileria import CapturarBooleano
from Utileria import BorrarPantalla

import AnMenu as Menu

# Función Main --------------------------------------------------------------
def Main():

    # Ciclo principal del programa:
    continuar = True

    while (continuar):

        BorrarPantalla()

        # Imprimimos el titulo
        print ("========== APROXIMAR RAICES ==========\n")

        # Capturamos el método de aproximación que queremos usar.
        metodoDeAproximacion = Menu.CapturarMetodoDeAproximacion()

        # Inicializamos el valor de a_n
        a = CapturarNumeroReal("\nIntroduce el valor de a: ")

        if ( EsRaiz(a) ):
            print("La raíz es: ", a)
            break

        # Inicializamos el valor de b_n
        b = CapturarNumeroReal("Introduce el valor de b: ")

        if ( EsRaiz(b) ):
            print("La raíz es: ", b)
            break

        # Verificamos que haya cambio de signo en el intervalo
        if ( HayCambioDeSignoEn(a, b) ):

            # Capturamos el tipo de aproximacion, iteraciones o truncamiento
            eleccionUsuario = Menu.CapturarTipoDeAproximacion()


            # Seleccionamos según el método y tipo de aproximación.
            if (metodoDeAproximacion == MetodosDeAproximacion.BISECCION):

                if (eleccionUsuario == Menu.OpcionMenu.ITERACIONES):
                    numeroDeIteraciones = Menu.CapturarNumeroDeIteraciones()
                    BorrarPantalla() # Limpiamos la pantalla

                    # Imprimimos el titulo
                    print ("========== BISECCIÓN ==========\n\n")

                    AproximarRaizPorIteraciones(a, b, numeroDeIteraciones, metodoDeAproximacion)

                elif (eleccionUsuario == Menu.OpcionMenu.ERROR_DE_TRUNCAMIENTO):
                    errorDeTruncamiento = Menu.CapturarErrorDeTruncamiento()
                    BorrarPantalla() # Limpiamos la pantalla

                    # Imprimimos el titulo
                    print ("========== BISECCIÓN ==========\n\n")

                    AproximarRaizErrorDeTruncamiento(a, b, errorDeTruncamiento, metodoDeAproximacion)


            elif (metodoDeAproximacion == MetodosDeAproximacion.FALSA_POSICION):

                if (eleccionUsuario == Menu.OpcionMenu.ITERACIONES):
                    numeroDeIteraciones = Menu.CapturarNumeroDeIteraciones()
                    BorrarPantalla() # Limpiamos la pantalla

                    # Imprimimos el titulo
                    print ("========== FALSA POSICIÓN ==========\n\n")

                    AproximarRaizPorIteraciones(a, b, numeroDeIteraciones, metodoDeAproximacion)

                elif (eleccionUsuario == Menu.OpcionMenu.ERROR_DE_TRUNCAMIENTO):
                    errorDeTruncamiento = Menu.CapturarErrorDeTruncamiento()
                    BorrarPantalla() # Limpiamos la pantalla

                    # Imprimimos el titulo
                    print ("========== FALSA POSICIÓN ==========\n\n")

                    AproximarRaizErrorDeTruncamiento(a, b, errorDeTruncamiento, metodoDeAproximacion)

        else:
            print("---> ERROR: No hay cambio de signo en el intervalo [", a, ", ", b, "].")

        continuar = CapturarBooleano("\n---> Presiona [Enter] para salir. Presiona [Cualquier tecla]+[Enter] para continuar: ")
# FIn Función Main ----------------------------------------------------------


# Ejecutamos el método Main
Main()