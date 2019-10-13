from Utileria import Enum
from Utileria import CapturarNumeroEntero
from Utileria import CapturarNumeroReal


# Crear una enumeración para los métodos de aproximación.
MetodosDeAproximacion = Enum( BISECCION = 0, FALSA_POSICION = 1, SIN_SELECCION = -1 )


# Creamos la enumeracion de las opciones del menú.
OpcionMenu = Enum( ITERACIONES = 0, ERROR_DE_TRUNCAMIENTO = 1, NO_SELECCION = 2)


# Función CapturarMetodoDeAproximacion --------------------------------------
def CapturarMetodoDeAproximacion():

     # Imprimir el menú.
    print ("\n> Selecciona el método de aproximación:\n[0]Bisección.\n[1]Falsa Posición.")

    # Capturar la elección del usuario.
    eleccionUsuario = MetodosDeAproximacion.SIN_SELECCION

    while( (eleccionUsuario != MetodosDeAproximacion.BISECCION) and (eleccionUsuario != MetodosDeAproximacion.FALSA_POSICION) ):
        eleccionUsuario = CapturarNumeroEntero("\n> Selección: ")

        if ( (eleccionUsuario != MetodosDeAproximacion.BISECCION) and (eleccionUsuario != MetodosDeAproximacion.FALSA_POSICION) ):
            print("\n---> ERROR: El valor no corresponde con ninguna opción.\n")

    return eleccionUsuario
#  Fin Función CapturarMetodoDeAproximacion ---------------------------------


# Función CapturarTipoDeAproximacion ----------------------------------------
def CapturarTipoDeAproximacion():

    # Imprimir el menú.
    print ("\n> Selecciona el tipo de aproximación:\n[0]Aproximar por Iteraciones.\n[1]Aproximar por Error de truncamiento.")

    # Capturar la elección del usuario.
    eleccionUsuario = OpcionMenu.NO_SELECCION

    while( (eleccionUsuario != OpcionMenu.ITERACIONES) and (eleccionUsuario != OpcionMenu.ERROR_DE_TRUNCAMIENTO) ):
        eleccionUsuario = CapturarNumeroEntero("\n> Selección: ")

        if ( (eleccionUsuario != OpcionMenu.ITERACIONES) and (eleccionUsuario != OpcionMenu.ERROR_DE_TRUNCAMIENTO) ):
            print("\n---> ERROR: El valor no corresponde con ninguna opción.\n")

    return eleccionUsuario

# Fin Función CapturarTipoDeAproximacion -----------------------------------


# Función CapturarNumeroDeIteraciones ---------------------------------------
def CapturarNumeroDeIteraciones():

    # Capturamos el número de iteraciones
    numeroDeIteraciones = 0
    while ( numeroDeIteraciones <= 0 ):
        numeroDeIteraciones = CapturarNumeroEntero("\nIntroduce el número de iteraciones: ")

        if (numeroDeIteraciones <= 0):
            print("\n---> ERROR: El número de iteraciones no puede ser menor o igual a cero.\n")

    return numeroDeIteraciones
# Fin Función CapturarNumeroDeIteraciones -----------------------------------


# Función CapturarErrorDeTruncamiento ---------------------------------------
def CapturarErrorDeTruncamiento():

    # Capturamos el error
    errorDeTruncamiento = 0.0

    while ( errorDeTruncamiento <= 0 ):
        errorDeTruncamiento = CapturarNumeroReal("\nIntroduce el error de truncamiento: ")

        if ( errorDeTruncamiento <= 0 ):
            print("\n---> ERROR: El error de truncamiento no puede ser menor o igual a cero.\n")

    return errorDeTruncamiento
#  Fin Función CapturarErrorDeTruncamiento ----------------------------------
