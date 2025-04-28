# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 18/03/2025 08:00
# Última modificación: 18/03/2025 09:41
# Versión de python: 3.13.2
from logging import raiseExceptions

def determinarMayor(pnum):
    """
    Funcionamiento:
    -Mientras pnum sea mayor que 0 se realiza el siguiente proceso:
    -A la variable residuo se le asigna el contenido de la operación, en este caso el residuo
    -Se pregunta que si el residuo es mayor a la variable numM
    -Si pasa, a numM se le asigna el contenido de Residuo
    -Se le hace una division entera a pnum para decrementar su valor.
    Entradas:
    -pnum(str): Contiene el número ingresado con valor int.
    Salidas:
    -Se retorna un string indicando cúal es el número mayor.
    """
    numM = 0
    residuo = 0
    while pnum >0:                          # Ciclo que se ejecuta mientras pnum sea mayor que 0
        residuo=pnum%10                     # Se le asigna a la variable el residuo de la operación
        if residuo > numM:                  # Si el residuo es mayor al numero Mayor actual, se le asigna al numero Mayor el residuo
            numM = residuo
        pnum=pnum//10
    return "El numero mayor es: "+str(numM) # Se retorna el número mayor

def determinarMayorAux(pnum):
    """
    Funcionamiento:
    -Se evalua que el número no venga vacio.
    -Si no contuviese nada, se manda una excepción TypeError y lo devuelve a ingresar nuevamente el número.
    -Se cambia el tipo valor de la variable a int, para poder hacer la operación matematica.
    -Si ocurriese algún ValueError, salta la excepción y lo devuelve a ingresar nuevamente el número.
    Entradas:
    -pnum(str): Contiene el número ingresado.
    Salidas:
    -Se retorna lo que contiene la función determinarMayor
    """
    try:
        if not pnum.strip():                # Se prueba que el contenido no este vacio
            raise TypeError                 # Se crea el error TypeError en caso de que el contenido este vacío
        nume = int(pnum)
        return (determinarMayor(nume))
    except TypeError:                       # Saltan las excepciones en caso de ser necesarias
        print("Debe ingresar un valor numérico \n")
        return determinarMayorES()          # Vuelve a hacer el proceso de ingresar el valor, hasta que esté correcto
    except ValueError:
        print("El valor debe ser únicamente entero \n")
        return determinarMayorES()

def determinarMayorES():
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    -N/A
    Salidas:
    -Se retorna lo que contiene la función determinarMayorAux.
    """
    num = str
    num=input("Ingrese un numero: ")        # Se ingresa el número, en este caso con valor string
    return determinarMayorAux(num)

print(determinarMayorES())