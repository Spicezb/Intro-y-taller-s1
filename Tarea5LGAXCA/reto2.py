# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 23/03/2025 21:00
# Última modificación: 23/03/2025 21:32
# Versión de python: 3.13.2

#Definición de funciones
def convDecimalOctal(pnum):
    """
        Funcionamiento:
        -Mientras pnum sea mayor a 0, se realiza el siguiente proceso:
        -A la variable octal, se le agrega en str lo que contiene la operación, luego se le suma lo que contienen octal.
        -La operación pnum%8 me da el residuo, que es el número octal equivalente que necesitamos.
        -Luego pnum//=8, ya que estamos trabajando en base 8.
        Entradas:
        -pnum(int): Contiene el número ingresado.
        Salidas:
        -Se retorna el número octal, en forma de string.
    """
    octal=""
    while pnum>0:                                       # Se procesa el ciclo, y se convierte el número a base octal.
        octal=str(pnum%8)+octal
        pnum//=8
    return octal

def convDecimalOctalAux(pnum):
    """
        Funcionamiento:
        -Se evalua que el número sea mayor a 0.
        -Si fuese menor, salta la excepción.
        Entradas:
        -pnum(int): Contiene el número ingresado.
        Salidas:
        -Se retorna lo que contiene la función convDecimalOctal.
    """
    if pnum<0:                                          # Si el número es menor a 0, se indica que debe ser mayor.
        return "Debe indicar un número mayor a 0."
    return convDecimalOctal(pnum)

def convDecimalOctalES(num):
    """
        Funcionamiento:
        -Se pide que se ingrese un número para poder evaluarlo.
        Entradas:
        - num(int): Es el número a convertir a base octal.
        Salidas:
        -Se retorna lo que contiene la función convDecnialOctalAux.
    """
    try:
        #num=int(input("Ingrese un número: "))          # Se le pide al usuario que ingrese un número.
        return convDecimalOctalAux(num)
    except:
        return "Debe indicar un número entero."         # Si ocurre un error en la ejecucion, salta la excepción.

#Código principal
print(convDecimalOctalES("Asd"))
print(convDecimalOctalES(-45))
print(convDecimalOctalES(786))
print(convDecimalOctalES(199))
print(convDecimalOctalES(19782))