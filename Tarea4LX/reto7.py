# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 18/03/2025 8:30
# Última modificación: 18/03/2025 09:16
# Versión de python: 3.13.2

#Definición de funciones
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

def elevarNumeroES():
    """
    Funcionamiento:
    - Recibe la base y el exponente que ingresa el usuario y llama la función auxiliar.
    Entradas:
    - N/A
    Salidas:
    - "La base y el exponente deben ser enteros \n"(str): Significa que la base o el exponente no fueron enteros.\
    - Llama la función auxiliar.
    """
    while True:
        try:
            base=exponente=0
            base=int(input("Ingrese la base que desea elevar: "))
            exponente=int(input("Ingrese el exponente al que desea elevar la base: "))
            return elevarNumeroAux(base,exponente)
        except ValueError:
            print("La base y el exponente deben ser enteros \n")

#Código principal
print(elevarNumeroES())
#Fin del código