# Elaborado por: Xavier Céspedes Alvarado

#Definición de funciones
def esPar(pnum):
    if pnum%2==0:
        return True
    return False

def contarDigitos(pnum):
    contador=0
    while pnum>0:
        pnum//=10
        contador+=1
    return contador

def voltearNumero(pnum):                       #Se agrega la función voltearNumero.
    numVol=0
    while pnum>0:
        numVol=numVol*10 + pnum%10
        pnum//=10
    return numVol

#Reto 1: Extraer par o impar según se indica.
def obtenerValores(pcifra,pindice,paridad):
    resultado=0
    pcifra//=(10**(pindice-1))
    while pcifra>0:
        if paridad==0:
            if esPar(pcifra)==True:
                resultado=resultado*10 + pcifra%10
        else:
            if esPar(pcifra)==False:
                resultado=resultado*10 + pcifra%10
        pcifra//=10
    return voltearNumero(resultado)            #Originalmente retornaba el resultado en orden inverso.

def obtenerValoresAux(pcifra,pindice,paridad):
    if type(pcifra)!=int or type(pindice)!=int or type(paridad)!=int:
        return "Todos los valores de ingreso deben ser enteros."
    elif contarDigitos(pcifra)<3:
        return "La cifra de análisis, debe ser un entero mayor o igual a 3 dígitos."
    elif pindice<1:
        return "Deb indicar una posición mayor o igual a 1."
    elif paridad<0 or paridad>1:
        return "Solo es posible extraer pares e impares."
    elif contarDigitos(pcifra)<pindice:
        return "La cifra numérica no posee esa cantidad de dígitos."
    return obtenerValores(pcifra,pindice,paridad)

def obtenerValoresES(pcifra,pindice,paridad):
    try:
        return obtenerValoresAux(pcifra,pindice,paridad)
    except:
        print("Todos los valores de ingreso deben ser enteros.")
    return ""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Reto 2: Subconjuntos numéricos.
def esSubConjunto(psub,pnumero):
    while psub>0:
        pnumCopia=pnumero
        existe=False
        while pnumCopia>0:
            if psub%10==pnumCopia%10:
                existe=True
            pnumCopia//=10
        if existe==False:
            return False
        psub//=10
    return True

def esSubConjuntoAux(psub,pnumero):
    if psub<1 or pnumero<1:
        return "Ambos valores deben ser mayores a 0."
    elif type(psub)!=int or type(pnumero)!=int:
        return "Ambos valores deben ser enteros."
    return esSubConjunto(psub,pnumero)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Reto 3: Obtener secuencia.
def obtenerSecuencia(pnumero):
    resultado = 0
    contador = 1
    while contador <= pnumero:
        resultado += (contador+1)/(pnumero**2)
        contador +=1
    return resultado

def obtenerSecuenciaAux(pnumero):
    if pnumero<=0:
        return "El valor del número debe ser mayor a 0."
    elif type(pnumero)!=float and type(pnumero)!=int:
        return "El valor solo puede ser entero o flotante"
    return obtenerSecuencia(pnumero)

def obtenerSecuenciaES(pnumero):
    try:
        return obtenerSecuenciaAux(pnumero)
    except:
        print("El valor debe ser entero o flotante.")
    return ""
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#hsdfgshdgkfsgkfg
#Código principal
#Reto 1: Extraer par o impar según se indica.
print("\n Reto 1: Extraer par o impar según se indica.")

print("Para la entrada: '78',5,1")
print(obtenerValoresES("78",5,1))

print("Para la entrada: 78,'5',1")
print(obtenerValoresES(78,"5",1))

print("Para la entrada: 78,5,'1'")
print(obtenerValoresES(78,5,"1"))

print("Para la entrada: 78,5,1")
print(obtenerValoresES(78,5,1))

print("Para la entrada: 12345678,0,1")
print(obtenerValoresES(12345678,0,1))

print("Para la entrada: 12345678,4,2")
print(obtenerValoresES(12345678,4,2))

print("Para la entrada: 678,5,1")
print(obtenerValoresES(678,5,1))

print("Para la entrada: 12345678,4,1")
print(obtenerValoresES(12345678,4,1))

print("Para la entrada: 12345678,4,0")
print(obtenerValoresES(12345678,4,0))

print("Para la entrada: 2345678,2,1")
print(obtenerValoresES(2345678,2,1))

print("Para la entrada: 345678,1,0")
print(obtenerValoresES(345678,1,0))

#Reto 2: Subconjuntos numéricos.
print("\n Reto 2: Subconjuntos numéricos.")

print("Para la entrada: 915,241593")
print(esSubConjuntoAux(915,241593))

print("Para la entrada: 89,12345678")
print(esSubConjuntoAux(89,12345678))

print("Para la entrada: 6421,12345678")
print(esSubConjuntoAux(6421,12345678))

print("Para la entrada: 1,2345678")
print(esSubConjuntoAux(1,2345678))

print("Para la entrada: 1,-10")
print(esSubConjuntoAux(1,-10))

#Reto 3: Obtener secuencia.
print("\n Reto 3: Obtener secuencia.")

print("Para la entrada: 0")
print(obtenerSecuenciaES(0))

print("Para la entrada: 2")
print(obtenerSecuenciaES(2))

print("Para la entrada: 6")
print(obtenerSecuenciaES(6))

print("Para la entrada: 8")
print(obtenerSecuenciaES(8))