import os as OperativeSystem

# Función CapturarNumeroReal ------------------------------------------------
def CapturarNumeroReal(mensaje):
    while(True):
        try:
            numero = float(input(str(mensaje)))
            return numero
        except ValueError:
            print("\n---> ERROR: El valor introducido no se puede representar como un número real.")
# Fin Función CapturarNumeroReal --------------------------------------------


# Función CapturarNumeroEntero ----------------------------------------------
def CapturarNumeroEntero(mensaje):
    while(True):
        try:
            numero = int(input(str(mensaje)))
            return numero
        except ValueError:
            print("\n---> ERROR: El valor introducido no se puede representar como un número entero.")
# Fin Función CapturarNumeroEntero ------------------------------------------


# Función CapturarBooleano --------------------------------------------------
def CapturarBooleano(mensaje):
    while(True):
        try:
            numero = bool(input(str(mensaje)))
            return numero
        except:
            print("\n---> ERROR: El valor introducido no se puede representar como un booleano.")
# Fin Función CapturarBooleano ----------------------------------------------


# Función Enum --------------------------------------------------------------
def Enum(**enums):
    return type('Enum', (), enums)
# Fin Función Enum ----------------------------------------------------------


# Función BorrarPantalla ----------------------------------------------------
def BorrarPantalla():
    clear = lambda: OperativeSystem.system('cls') # Borrar la pantalla para windows
    clear()
# Fin Función BorrarPantalla -----------------------------------------------