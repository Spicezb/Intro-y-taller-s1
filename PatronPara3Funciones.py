#Elaborado por: XXX XXX XXX
#Fecha de creación: dd/mm/aaaa hh:mm
#última modificación:  dd/mm/aaaa hh:mm
#Versión: 3.10.2

#Definición de Funciones
#----------------------------------------------------
#Reto#0: Contar Digitos
def contarDigitos(pnum):
    """
    Funcionamiento:
    - Cuenta los dígitos de una cifra.
    Entradas:
    - pnum(int):la cifra numérica.
    Salidas:
    - (int) la cantidad de dígitos de la frase
    """
    contador=0
    while pnum!=0:
        contador+=1
        pnum=pnum//10
    return contador

def contarDigitosAux(pnum):
    """
    ... 
    """
    if isinstance(pnum,int)==True:
        if pnum<0:
            #En la función de validación debe construir los textos de salida correctos....
            return "La cifra que ingresó, tiene: "+str(contarDigitos(abs(pnum)))+" digito(s)."
        else:
            return "La cifra que ingresó, tiene: "+str(contarDigitos(pnum))+" digito(s)."
    else:
        return "Debe ingresar una cifra numérica."

def contarDigitosES(num):
    """
    ... 
    """
    continua= True
    while continua:
        try:
            #num=int(input("Indique una cifra numérica: "))
            print(contarDigitosAux(num))
            continua = False
        except:
            print("Debe ingresar un número entero.")
    return ""
#----------------------------------------------------
#Reto#3: Encontrar al menos un cero en un número
def encontrarAlmenosUnCero(pnumero):
    """
    ...
    """
    while pnumero>0:
        digito=pnumero%10
        if digito==0:
            return True
        pnumero//=10
    return False

def encontrarAlmenosUnCeroAux(pnumero):
    """
    ...
    """
    if encontrarAlmenosUnCero(pnumero) ==True:
        return "La cifra numérica posee al menos un cero."
    return "La cifra numérica NO posee ningún cero."

def encontrarAlmenosUnCeroES(num):
    """
    ...
    """
    continua= True
    while continua:
        try:
            #num=int(input("Indique una cifra numérica: "))
            print(encontrarAlmenosUnCeroAux(num))
            continua = False
        except:
            print("Debe ingresar un número entero.")
    return ""

#Programa principal
#Reto#0: Contar Digitos
print("\n**Reto#0: Contar Digitos**")
x= ""
print("Para la entrada:",x)
print(contarDigitosES(x))
x=1203423
print("Para la entrada:",x) 
print(contarDigitosES(x))
x=3405403465
print("Para la entrada:",x)
print(contarDigitosES(x))
#llame cada reto según los escenarios que muestra la especificación, ejemplo:
#Reto#3: Encontrar al menos un cero en un número
print("\n**Reto#3: Encontrar al menos un cero en un número**")
x=876543
print("Para la entrada:",x)
print(encontrarAlmenosUnCeroES(x))
x=1203423
print("Para la entrada:",x)
print(encontrarAlmenosUnCeroES(x))
x=3405403465
print("Para la entrada:",x)
print(encontrarAlmenosUnCeroES(x))



