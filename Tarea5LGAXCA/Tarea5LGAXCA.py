# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 23/03/2025 21:11
# Última modificación: 24/03/2025 20:19
# Versión de python: 3.13.2

#Definición de funciones
#--------------------------------------------------------------------------------------------------------------------
#Reto #1: Diferencia entre valores extremos.
def diferenciarExtremos(pnumero):
    """
    Funcionamiento:
    - Identifica el dígito mayor y menor, para sacar la diferencia entre ellos.
    Entradas:
    - pnumero(int): Es el número del que se van a sacar los dígitos.
    Salidas:
    - mayor(int): Es el dígito mayor.
    - menor(int): Es el dígito menor.
    """
    mayor=0
    menor=9
    while pnumero>0:
        if pnumero%10>mayor:
            mayor = pnumero%10
            if menor>pnumero%10:          #Hay un doble if porque pnumero puede ser el menor y el mayor a la vez.
                menor = pnumero%10
        elif menor>pnumero%10:
                menor = pnumero%10
        pnumero//=10
    return mayor, menor

def diferenciarExtremosAux(pnumero):
    """
    Funcionamiento:
    - Verifica que pnumero sea entero y llama la función principal.
    Entradas:
    - pnumero(int): Es el número del que se van a sacar los dígitos.
    Salidas:
    - "El número debe ser mayor que cero"(str): El número ingresado no fue mayor que cero.
    - "El valor debe ser únicamente un número entero"(str): No se ingresó un número entero.
    - Llama a la función principal y retorna un str con el resultado final.
    """
    if isinstance(pnumero,int):              #Verifica que pnumero sea entero.
        if pnumero<0:
            return "El número debe ser mayor que cero"
        mayor, menor = diferenciarExtremos(pnumero)
        return "El número mayor es: "+str(mayor)+", el menor es: "+str(menor)+", la diferencia es: "+str(mayor-menor)
    else:
        return "El valor debe ser únicamente un número entero"

def diferenciarExtremosES(pnumero):
    """
    Funcionamiento:
    - Recibe el número del que se van a sacar los dígitos y llama la función auxiliar.
    Entradas:
    - pnumero(int): Es el número del que se van a sacar los dígitos.
    Salidas:
    - ""(str): Retorna un string vacío después de imprimir la función auxiliar.
    """
    continua = True
    while continua:
        try:
            #pnumero = int(input("Ingrese un número: "))
            continua = False
            print(diferenciarExtremosAux(pnumero))
        except:
            print("El número debe ser entero")
    return ""
#--------------------------------------------------------------------------------------------------------------------
#Reto #2: Convertir de decimal a octal.
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
    continua=True
    while continua:
        try:
            #num=int(input("Ingrese un número: "))          # Se le pide al usuario que ingrese un número.
            continua = False
            print(convDecimalOctalAux(num))
        except:
            print("Debe indicar un número entero.")   # Si ocurre un error en la ejecucion, salta la excepción.
    return ""      
#--------------------------------------------------------------------------------------------------------------------
#Reto #3: Número palíndromo.
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
    continua = True
    while continua:
        try:
            #num=int(input("Ingrese un número: "))          # Se le pide al usuario que ingrese un número.
            continua=False
            print(numPalindromoAux(num)) 
        except:
            print("Debe de ingresar un valor numérico")        # Si ocurre un error en la ejecucion, salta la excepción.
    return ""   
#--------------------------------------------------------------------------------------------------------------------
#Reto #4: Diferencia de dígitos entre 2 números.
def diferenciarDigitos(pnumero1,pnumero2):
    """
    Funcionamiento:
    - Determina cuales dígitos de un número no están en otro número; si todos están, retorna False.
    Entradas:
    - pnumero1(int): Es el primer número, del que se tiene que saber cuales dígitos no están en el otro número.
    - pnumero2(int): Es el número con el que se verifica que no coincidan los dígitos del primero.
    Salidas:
    - False si no hay dígitos que no estén en el segundo número.
    - resultado(str): Son los dígitos que están en el primer número y no en el segundo.
    """
    resultado = ""
    num2 = pnumero2
    while pnumero1>0:
        while pnumero2>0:
            if pnumero1%10==pnumero2%10:
                pnumero1//=10
                pnumero2=num2   #pnumero2 se resetea a su valor original
            pnumero2//=10
        if pnumero1%10!=0:      #En la última vuelta el residuo puede ser 0, pero no tiene que ser concatenado.
            resultado = str(pnumero1%10) + resultado
        pnumero1//=10
        pnumero2=num2
    if resultado == "":
        return False
    return resultado

def diferenciarDigitosAux(pnumero1,pnumero2):
    """
    Funcionamiento:
    - Verifica que los números sean enteros y mayores que 0, llama la función principal.
    Entradas:
    - pnumero1(int): Es el primer número, del que se tiene que saber cuales dígitos no están en el otro número.
    - pnumero2(int): Es el número con el que se verifica que no coincidan los dígitos del primero.
    Salidas:
    - "Debe indicar números enteros"(str): Si alguno de los números no fue entero.
    - "Los números deben ser mayores a cero"(str): Si alguno de los números fue igual o menor a 0.
    - Llama la función principal.
    """
    if type(pnumero1)!=int or type(pnumero2)!=int:
        return "Debe indicar números enteros"
    elif pnumero1<1 or pnumero2<1:
        return "Los números deben ser mayores a cero"
    elif diferenciarDigitos(pnumero1,pnumero2)==False:
        return False
    return "El resultado es " + str(diferenciarDigitos(pnumero1, pnumero2))

def diferenciarDigitosES(pnumero1,pnumero2):
    """
    Funcionamiento:
    - Recibe los números que se van a evaluar.
    Entradas:
    - pnumero1(int): Es el primer número, del que se tiene que saber cuales dígitos no están en el otro número.
    - pnumero2(int): Es el número con el que se verifica que no coincidan los dígitos del primero.
    Salidas:
    - "Debe indicar números enteros"(str): Si alguno de los valores ingresados no fue entero.
    - Llama la función auxiliar.
    """
    continua = True
    while continua:
        try:
            #pnumero1 = int(input("Ingrese un número: "))
            #pnumero2 = int(input("Ingrese otro número: "))
            print(diferenciarDigitosAux(pnumero1,pnumero2))
            continua = False
        except:
            print("Debe indicar números enteros")
    return ""
#--------------------------------------------------------------------------------------------------------------------

#Código principal
#--------------------------------------------------------------------------------------------------------------------
#reto #1: Diferencia entre valores extremos
print("\n**Reto #1: Diferencia entre valores extremos**")
x = ""
print("Para la entrada:",x)
print(diferenciarExtremosES(x))
x = 876543
print("Para la entrada:",x) 
print(diferenciarExtremosES(x))
x = 1203423
print("Para la entrada:",x)
print(diferenciarExtremosES(x))
x = 3454193465
print("Para la entrada:",x)
print(diferenciarExtremosES(x))
#--------------------------------------------------------------------------------------------------------------------
#reto #2: Convertir de decimal a octal
print("\n**Reto #2: Convertir de decimal a octal**")
x = "Asd"
print("Para la entrada:", x)
print(convDecimalOctalES(x))
x = -45
print("Para la entrada:", x)
print(convDecimalOctalES(x))
x = 786
print("Para la entrada:", x)
print(convDecimalOctalES(x))
x = 199
print("Para la entrada:", x)
print(convDecimalOctalES(x))
x = 19782
print("Para la entrada:", x)
print(convDecimalOctalES(x))
#--------------------------------------------------------------------------------------------------------------------
#reto #3: Número palíndromo
print("\n**Reto #3: Número palíndromo**")
x = 161
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 2992
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 3003
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 2882
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 28821
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 128821
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 61
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 66
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 660
print("Para la entrada:", x)
print(numPalindromoES(x))
x = 7
print("Para la entrada:", x)
print(numPalindromoES(x))
#--------------------------------------------------------------------------------------------------------------------
#reto #4: Diferencia de dígitos entre 2 números.
print("\n**Reto #4: Diferencia de dígitos entre 2 números**")
x="1234"
y="23"
print("Para la entrada:",(x,y))
print(diferenciarDigitosES(x,y))
x=136
y=-12
print("Para la entrada:",(x,y))
print(diferenciarDigitosES(x,y))
x=29837
y=321
print("Para la entrada:",(x,y))
print(diferenciarDigitosES(x,y))
x=23
y=3218
print("Para la entrada:",(x,y))
print(diferenciarDigitosES(x,y))
x=6328
y=6817
print("Para la entrada:",(x,y))
print(diferenciarDigitosES(x,y))
#--------------------------------------------------------------------------------------------------------------------