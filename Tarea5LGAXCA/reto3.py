# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 23/03/2025 21:32
# Última modificación: 23/03/2025 22:11
# Versión de python: 3.13.2
def numPalindromo(pnum):
    """
        Funcionamiento:
        -Mientras pnum sea mayor a 0, se realiza el siguiente proceso:
        -A la variable num, se le agrega lo que contiene la operación.
        -La operación pnum%10 me da el número menos significativo, y lo coloco primero en el nuevo numero(num).
        -Si el número original es igual al nuevo número(nuevoN), retorna True
        Entradas:
        -pnum(int): Contiene el número ingresado.
        Salidas:
        -Se retorna el True o False, depende si el número es palíndromo.
    """
    nuevoN=""
    numOri=pnum
    while pnum>0:
        nuevoN+=str(pnum%10)
        pnum//=10
    if str(numOri) == nuevoN:
        return True
    return False

def numPalindromoAux(pnum):
    """
        Funcionamiento:
        -Se evalua que el número sea mayor a 9.
        -Si fuese menor, salta la excepción.
        Entradas:
        -pnum(int): Contiene el número ingresado.
        Salidas:
        -Se retorna lo que contiene la función numPalindromo.
    """
    if pnum<9:
        return "Indique un número válido."
    return numPalindromo(pnum)

def numPalindromoES(num):
    """
        Funcionamiento:
        -Se pide que se ingrese un número para poder evaluarlo.
        Entradas:
        - num(int): Es el número a evaluar si es palíndromo.
        Salidas:
        -Se retorna lo que contiene la función numPalindromoAux.
    """
    while True:
        try:
            #num=int(input("Ingrese un número: "))          # Se le pide al usuario que ingrese un número.
            return numPalindromoAux(num)
        except:
            return "Debe de ingresar un valor numérico"     # Si ocurre un error en la ejecucion, salta la excepción.

#Código principal
print(numPalindromoES(161))
print(numPalindromoES(2992))
print(numPalindromoES(3003))
print(numPalindromoES(2882))
print(numPalindromoES(28821))
print(numPalindromoES(128821))
print(numPalindromoES(61))
print(numPalindromoES(66))
print(numPalindromoES(660))
print(numPalindromoES(7))