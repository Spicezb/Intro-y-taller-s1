def esPar(num):
    if num%2==0:
        return True
    return False

def contarDigitos(num):
    contador=0
    while num>0:
        num//=10
        contador+=1
    return contador

def voltearNumero(num):
    numVol=0
    while num>0:
        numVol=numVol*10 + num%10
        num//=10
    return numVol

