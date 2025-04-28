# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 18/03/2025 09:42
# Última modificación: 18/03/2025 10:38
# Versión de python: 3.13.2

def esNumeroPrimo(pnum):
    """
    Funcionamiento:
    - Mientras la variable conta que contiene el valor de pnum, se pregunta si el residuo de conta entre pnume da 0
    - Si da 0, el conta2 se le suma 1, este lleva las veces que es divisible el número.
    - Si el conta2 es igual a 2 significa que es solo divisible entre 2 números, haciendolo primo.
    Entradas:
    -pnum(int): Contiene el número ingresado.
    Salidas:
    -Se retorna lo que contiene la función determinarMayor
    """
    conta = pnum
    conta2 = 0
    while conta >= 1:                               # El ciclo se ejecuta mientras sea conta sea menor o igual a 1
        if pnum%conta == 0:                         # Si el residuo de la operación de 0, conta2 se incrementa 1
            conta2 +=1                              # Si al final conta2 es igual a 2, el numero es primo.
        conta-=1
    if conta2 == 2:
        return "El número es primo"
    return "El número no es primo"

def esNumeroPrimoAux(pnum):
    """
    Funcionamiento:
    -Se evalúa que el número no venga vacío.
    -Si no contuviese nada, se manda una excepción TypeError y lo devuelve a ingresar nuevamente el número.
    -Se cambia el tipo valor de la variable a int, para poder hacer la operación matematica.
    -Si ocurriese algún ValueError, salta la excepción y lo devuelve a ingresar nuevamente el número.
    -Se evalúa que el número no sea menor o igual a 0.
    Entradas:
    -pnum(str): Contiene el número ingresado.
    Salidas:
    -Se retorna lo que contiene la función esNumeroPrimo.
    """
    try:
        if not pnum.strip():                        # Se prueba que el contenido no este vacio
            raise TypeError                         # Se crea el error TypeError en caso de que el contenido este vacío
        pnume = int(pnum)
        if pnume <=0 :                              # Se pregunta si el número es menor o igual a 0
            print("El numero debe ser mayor a 1 \n")
            return esNumeroPrimoES()                # Si es igual o menor a 0, se vuelve a hacer el proceso de ingresar el número
        return esNumeroPrimo(pnume)
    except TypeError:                               # Saltan las excepciones en caso de ser necesarias
        print("Debe ingresar un valor numérico \n")
        return esNumeroPrimoES()                    # Vuelve a hacer el proceso de ingresar el valor, hasta que esté correcto
    except ValueError:
        print("El valor debe ser únicamente entero \n")
        return esNumeroPrimoES()


def esNumeroPrimoES():
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    -N/A
    Salidas:
    -Se retorna lo que contiene la función esNumeroPrimoAux.
    """
    while True:
            num = str
            num=input("Ingrese un numero: ")        # Se ingresa el número a evaluar, en string para luego hacerle validaciones
            return (esNumeroPrimoAux(num))

print(esNumeroPrimoES())