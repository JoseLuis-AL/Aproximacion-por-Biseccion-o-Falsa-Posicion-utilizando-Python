from prettytable import PrettyTable as PTable
from Utileria import Enum
import math as Calcular


# Crear una enumeración para los métodos de aproximación.
MetodosDeAproximacion = Enum( BISECCION = 0, FALSA_POSICION = 1 )


# Función f -----------------------------------------------------------------
def f(x):
    try:
        return x + 1 # Inserte la función aquí
    except:
        print ("\n---> ERROR: No es posible evaluar la función.")
        return False
# Fin Función f -------------------------------------------------------------


# Función HayCambioDeSignoEn ------------------------------------------------
def HayCambioDeSignoEn(_a, _b):
    return ( (f(_a) > 0 and f(_b) < 0) or (f(_a) < 0 and f(_b) > 0) )
# Fin Función HayCambioDeSignoEn --------------------------------------------


# Función EsRaiz ------------------------------------------------------------
def EsRaiz(_x):
    return True if (f(_x) == 0) else False
# Fin Función EsRaíz --------------------------------------------------------


# Función AproximarRaizPorIteraciones ---------------------------------------
def AproximarRaizPorIteraciones(_a, _b, _numeroDeIteraciones, _metodo):

    # Creamos la tabla donde se almacenarán los resultados.
    tablaResultados = PTable(['n', 'a', 'b', 'x_n', 'f(x_n)'])

    a_n = _a          # Definimos el extremo a_n del intervalo [a_n, b_n].
    b_n = _b          # Definimos el extremo b_n del intervalo [a_n, b_n].

    x_n = 0.0         # Inicializamos el valor del punto medio del intervalo.
    fx_n = 0.0        # Inicializamos el valor de f(x_n)
    iteraciones = 0   # Inicializamos el número de iteraciones.

    # Si ninguno de los extremos es una raíz, procedemos a verificar el intervalo.
    if (not(EsRaiz(a_n)) and not(EsRaiz(b_n))):

        # Comprobar que el método exista.
        if ( (_metodo == MetodosDeAproximacion.FALSA_POSICION) or (_metodo == MetodosDeAproximacion.BISECCION) ):

            # Si hay cambio de signo en el intervalo, procedemos a aplicar el método de bisección.
            if (HayCambioDeSignoEn(a_n, b_n)):

                # Ciclo para aproximar la raíz.
                while (iteraciones < _numeroDeIteraciones):

                    # Calculamos el valor de x_n dependiendo del método
                    if (_metodo == MetodosDeAproximacion.BISECCION):
                        x_n = (a_n + b_n) / 2

                    elif (_metodo == MetodosDeAproximacion.FALSA_POSICION):
                        x_n = a_n - ( f(a_n)*(b_n - a_n) ) / ( f(b_n) - f(a_n) )

                    # Calculamos el valor de f(x_n).
                    fx = f(x_n)

                    # Añadimos los datos a la tabla de resultados.
                    tablaResultados.add_row([iteraciones, a_n, b_n, x_n, fx])

                    # Definimos el nuevo intervalo.
                    b_n = x_n if (f(a_n) * fx < 0) else b_n
                    a_n = x_n if (f(b_n) * fx < 0) else a_n

                    # Verificamos si ya encontramos la raíz o necesitamos realizar una nueva iteración.
                    iteraciones = _numeroDeIteraciones if (fx == 0) else iteraciones + 1
            
                print (tablaResultados)
                print ("\n-----> La mejor aproximación es x_n = ", x_n, "\n\n")

            else:
                print ("\n--->ERROR: No es posible calcular x_n por el método indicado.")

        else:
            print ("\n---> ERROR: No hay cambio de signo en el intervalo.")
    else:
        if (EsRaiz(a_n)):
            print ("\n-----> El extremo del intervalo a_n = ", a_n, " es raíz exacta")
        if (EsRaíz(b_n)):
            print ("\n-----> El extremo del intervalo b_n = ", b_n, " es raíz exacta")
# Fin Función AproximarRaizPorIteraciones -----------------------------------


# Función AproximarRaizErrorDeTruncamiento ----------------------------------
def AproximarRaizErrorDeTruncamiento(_a, _b, _errorDeTruncamiento, _metodo):

    # Calcular el valor de k
    k = int( (Calcular.log( (_b - _a ) / _errorDeTruncamiento ) / Calcular.log(2)) ) + 1

    print ("Error de truncamiento: ", _errorDeTruncamiento)
    BiseccionPorIteraciones(_a, _b, k, _metodo)

# Fin Función AproximarRaizErrorDeTruncamiento ------------------------------
