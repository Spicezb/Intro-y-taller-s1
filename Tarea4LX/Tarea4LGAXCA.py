# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 18/03/2025 8:32
# Última modificación: 19/03/2025 18:21
# Versión de python: 3.13.2

#Definición de funciones
#--------------------------------------------------------------------------------------------------------------------
#Reto#6: Determinar el número mayor de la cifra númerica
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

def determinarMayorES(pnumero):
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    - pnumero(int): Es el número del que se va a encontrar el dígito mayor.
    Salidas:
    -Se retorna lo que contiene la función determinarMayorAux.
    """
    num = str
    #num=input("Ingrese un numero: ")        # Se ingresa el número, en este caso con valor string
    return determinarMayorAux(str(pnumero))
#--------------------------------------------------------------------------------------------------------------------
#Reto#7: Elevar un número a una potencia dada
def elevarNumero(pbase,pexponente):
    """
    Funcionamiento:
    - Eleva una base a un exponente dado.
    Entradas:
    - pbase(int): Es la base a ser elevada.
    - pexponente(int): Es el exponente al que va a ser elevada la base.
    Salidas:
    - Resultado(int): Es el resultado de elevar la base al exponente.
    """
    resultado=1
    while pexponente>0:
        resultado=resultado*pbase
        pexponente-=1                #Multiplica la base por si misma hasta que el exponente sea 0.
    return "El resultado es " + str(resultado)

def elevarNumeroAux(pbase,pexponente):
    """
    Funcionamiento:
    - Comprueba que la base y el exponente sean enteros mayores que cero.
    Entradas:
    - pbase(int): Es la base a ser elevada.
    - pexponente(int): Es el exponente al que va a ser elevada la base.
    Salidas:
    - "La base y el exponente deben ser iguales o mayores que cero \n"(str): la base o el exponente son negativos.
    - "La base y el exponente deben ser números enteros \n"(str): La base o  el exponente no son enteros.
    - Llama la función principal.
    """
    if pbase<0 or pexponente<0:
        print("La base y el exponente deben ser iguales o mayores que cero \n")
        return elevarNumeroES()
    elif type(pbase)!=int or type(pexponente)!=int:
        print("La base y el exponente deben ser números enteros \n")
        return elevarNumeroES()
    else:
        return elevarNumero(pbase,pexponente)

def elevarNumeroES(pbase,pexponente):
    """
    Funcionamiento:
    - Recibe la base y el exponente que ingresa el usuario y llama la función auxiliar.
    Entradas:
    - pbase(int): Es la base que se va a elevar.
    - pexponente(int): Es el exponente al que se va a elevar la base.
    Salidas:
    - "La base y el exponente deben ser enteros \n"(str): Significa que la base o el exponente no fueron enteros.\
    - Llama la función auxiliar.
    """
    while True:
        try:
            base=exponente=0
            #base=int(input("Ingrese la base que desea elevar: "))
            #exponente=int(input("Ingrese el exponente al que desea elevar la base: "))
            return elevarNumeroAux(pbase,pexponente)
        except ValueError:
            print("La base y el exponente deben ser enteros \n")
#--------------------------------------------------------------------------------------------------------------------
#Reto#8: Determinar si un número es primo o no
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

def esNumeroPrimoES(pnumero):
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    - pnumero(int): Es el número que se va a comprobar si es primo.
    Salidas:
    -Se retorna lo que contiene la función esNumeroPrimoAux.
    """
    while True:
            num = str
            #num=input("Ingrese un numero: ")        # Se ingresa el número a evaluar, en string para luego hacerle validaciones
            return (esNumeroPrimoAux(str(pnumero)))
#--------------------------------------------------------------------------------------------------------------------
#Reto#9: Sumar dígitos múltiplos
def sumarDigitosMultiplos(pnumero,pdigito):
    """
    Funcionamiento:
    - Eleva una base a un exponente dado.
    Entradas:
    - pnumero(int): Es el número del que se van a sumar los dígitos múltiplos del dígito.
    - pdigito(int): Es el digito del que se van a sumar los múltiplos.
    Salidas:
    - Resultado(int): Es el resultado de sumar los dígitos de pnumero que son múltiplos de pdigito.
    """
    resultado = 0
    while pnumero>0:
        if (pnumero%10)%pdigito==0:              #Si el último dígito de pnumero es múltiplo de pdigito
            resultado = resultado + pnumero%10
        pnumero = pnumero//10
    return "El resultado es " + str(resultado)

def sumarDigitosMultiplosAux(pnumero,pdigito):
    """
    Funcionamiento:
    - Comprueba que el número y el dígito sean enteros y mayores que 1.
    Entradas:
    - pnumero(int): Es el número del que se van a sumar los dígitos múltiplos del dígito.
    - pdigito(int): Es el digito del que se van a sumar los múltiplos.
    Salidas:
    - "El número y el dígito deben ser enteros \n"(str): El número o el dígito no fueron enteros.
    - "El número y el dígito deben ser mayores que 0 \n"(str): El número o el dígito no fueron mayores que 0.
    """
    if type(pnumero)!=int or type(pdigito)!=int:
        print("El número y el dígito deben ser enteros \n")
        return sumarDigitosMultiplosES()
    elif pnumero<1 or pdigito<1:
        print("El número y el dígito deben ser mayores que 0 \n")
        return sumarDigitosMultiplosES()
    else:
        return sumarDigitosMultiplos(pnumero,pdigito)

def sumarDigitosMultiplosES(pnumero,pdigito):
    """
    Funcionamiento:
    - Comprueba que el número y el dígito sean enteros y mayores que 1.
    Entradas:
    - pnumero(int): Es el número del que se van a sumar sus dígitos.
    - pdigito(int): Es el dígito del que se vana  sumar lo smúltiplos en el primer número.
    Salidas:
    - "El número y el dígito deben ser enteros \n"(str): El número o el dígito no son enteros.
    - Llama a la función auxiliar.
    """
    while True:
        try:
            numero=digito=0
            #numero=int(input("Ingrese un número: "))
            #digito=int(input("Ingrese un digito del que quiera sumar los múltiplos en el número anterior: "))
            return sumarDigitosMultiplosAux(pnumero,pdigito)
        except ValueError:
            print("El número y el dígito deben ser enteros \n")
#--------------------------------------------------------------------------------------------------------------------
#Reto#10: Es binario
def esBinario(pnum):
    """
    Funcionamiento:
    - Mientras la variable pnum sea mayor que 0.
    - A la variable num se le asigna el residuo de la division de pnum entre 10.
    - Si algún residuo da mayor de 1, el número pasa a no ser binario automáticamente
    Entradas:
    -pnum(int): Contiene el número ingresado.
    Salidas:
    - True: El número es binario
    - False: El número no es binario
    """
    while pnum >0:                       # El ciclo se ejecuta mientras pnum sea mayor que 0.
        if pnum%10 > 1:                  # Y si el residuo es mayor de 1, el número no es binario automáticamente.
            return False
        pnum=pnum//10
    return True

def esBinarioAux(pnum):
    """
    Funcionamiento:
    -Se evalúa que el número no venga vacío.
    -Si no contuviese nada, se manda una excepción TypeError y lo devuelve a ingresar nuevamente el número.
    -Se cambia el tipo valor de la variable a int, para poder hacer la operación matematica.
    -Si ocurriese algún ValueError, salta la excepción y lo devuelve a ingresar nuevamente el número.
    Entradas:
    -pnum(str): Contiene el número ingresado.
    Salidas:
    -Se retorna lo que contiene la función esBinario.
    """
    try:
        if not pnum.strip():                        # Se prueba que el contenido no este vacio
            raise TypeError                         # Se crea el error TypeError en caso de que el contenido este vacío
        nume = int(pnum)
        if esBinario(nume)==True:
            return "El número es binario"
        else:
            return "El número no es binario"
    except TypeError:                               # Saltan las excepciones en caso de ser necesarias
        print("Debe ingresar un valor numérico \n")
        return esBinarioES()                        # Vuelve a hacer el proceso de ingresar el valor, hasta que esté correcto
    except ValueError:
        print("El valor debe ser únicamente entero \n")
        return esBinarioES()

def esBinarioES(pnumero):
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    -pnumero(int): Es el número que se va a comprobar si es binario.
    Salidas:
    -Se retorna lo que contiene la función esBinarioAux.
    """
    num = str
    #num = input("Ingrese un número: ").strip()     # Se ingresa el número a evaluar, en string para luego hacerle validaciones
    return esBinarioAux(str(pnumero))
#--------------------------------------------------------------------------------------------------------------------
#Reto#11: Convertir a decimal
def convertirDecimal(pnumero):
    """
    Funcionamiento:
    - Convierte un número escrito en binario a decimal.
    Entradas:
    - pnumero(int): Es el número binario que se va a convertir a decimal.
    Salidas: 
    - resultado(int): Es el número en decimal.
    """
    contador = 0
    resultado = 0
    while pnumero>0:
        if (pnumero%10)==1:
            resultado = resultado + (2**contador)
        pnumero = pnumero//10
        contador = contador + 1
    return resultado

def convertirDecimalAux(pnumero):
    """
    Funcionamiento:
    - Verifica que el número ingresado sea binario.
    Entradas:
    - pnumero(int): Es el número binario que se va a convertir a decimal.
    Salidas: 
    - resultado(int): Es el número en decimal.
    """
    num = pnumero
    while pnumero > 0:                    # El ciclo se ejecuta mientras pnumero sea mayor que 0.                          
        if pnumero%10 > 1:            # Y si el residuo es mayor de 1, el número no es binario automáticamente.
            print("Debe ingresar un número binario \n")
            return convertirDecimalES()
        pnumero=pnumero//10
    return "El resultado es " + str(convertirDecimal(num))

def convertirDecimalES(pnumero):
    """
    Funcionamiento:
    - Recibe el número que se va a convertir a decimal y llama la función auxiliar
    Entradas:
    - pnumero(int): Es el número que se va a convertir a decimal.
    Salidas:
    - Llama la función auxiliar
    """
    while True:
        try:
            numero=0
            #numero=int(input("Ingrese un número binario para convertir a decimal: "))
            return convertirDecimalAux(pnumero)
        except ValueError:
            print("Debe ingresar un número entero \n")
#--------------------------------------------------------------------------------------------------------------------

#Código principal
#--------------------------------------------------------------------------------------------------------------------
#Reto#6: Determinar el número mayor de la cifra númerica
print("\n**Reto#6: Determinar el número mayor de la cifra númerica**")
print(determinarMayorES(1245))
#Reto#7: Elevar un número a una potencia dada
print("\n**Reto#7: Elevar un número a una potencia dada**")
print(elevarNumeroES(4,4))
#Reto#8: Determinar si un número es primo o no
print("\n**Reto#8: Determinar si un número es primo o no**")
print(esNumeroPrimoES(23))
#Reto#9: Sumar dígitos múltiplos
print("\n**Reto#9: Sumar dígitos múltiplos**")
print(sumarDigitosMultiplosES(666,3))
#Reto#10: Es binario
print("\n**Reto#10: Es binario**")
print(esBinarioES(1010))
#Reto#11: Convertir a decimal
print("\n**Reto#11: Convertir a decimal**")
print(convertirDecimalES(1010))