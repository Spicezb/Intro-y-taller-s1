# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 16/03/2025 20:03
# Última modificación: 16/03/2025 21:15
# Versión de python: 3.13.2

#Definición de funciones
def calcularCosto(ptipo,pedad,pdias):
    """
    Funcionamiento:
    - Calcula el costo de internación de un paciente dependiendo de su edad, su tipo de 
    enfermedad y la cantidad de días hospitalizado.
    Entradas:
    - ptipo(int): Significa el tipo de enfermedad.
    - pedad(int): Es la edad del paciente.
    - pdias(int): Son los días que el paciente estuvo hospitalizado.
    Salidas:
    - costo(float): Es el costo total de internación del paciente.
    """
    costo=0
    if ptipo==1:
        costo=pdias*25 
    elif ptipo==2:
        costo=pdias*16
    elif ptipo==3:
        costo=pdias*20
    elif ptipo==4:
        costo=pdias*32
    if 14<=pedad<=22:
        costo=costo*1.1
    return round(costo,2)

def calcularCostoAux(ptipo,pedad,pdias):
    """
    Funcionamiento:
    - Determina si las variables son de tipo entero, si el tipo está entre 1 y 4, si los días son
    mínimo 1 y si la edad es mínimo 0.
    Entradas:
    - ptipo(int): Significa el tipo de enfermedad.
    - pedad(int): Es la edad del paciente.
    - pdias(int): Son los días que el paciente estuvo hospitalizado.
    Salidas:
    - "El tipo, la edad y la cantidad de días deben ser enteros"(str): significa que alguna de
    las variables no fue entera.
    - "El tipo de enfermedad debe de estar entre 1 y 4"(str): Significa que el tipo de enfermedad no estuvo entre 1 y 4.
    - "La edad no puede ser menor a 0"(str): La edad ingresada fue menor a 0.
    - "La cantidad de días no puede ser menor a 1"(str): La cantidad de días ingresada fue menor a 1.
    - Llama a la función principal.
    """
    if type(ptipo)!=int or type(pedad)!=int or type(pdias)!=int: #Se verifica que las tres variables sean de tipo entero.
        return "El tipo, la edad y la cantidad de días deben ser enteros"
    elif ptipo<1 or ptipo>4:
        return "El tipo de enfermedad debe de estar entre 1 y 4"
    elif pedad<0:
        return "La edad no puede ser menor a 0"
    elif pdias<1:
        return "La cantidad de días no puede ser menor a 1"
    else:
        return calcularCosto(ptipo,pedad,pdias)

def calcularCostoES():
    """
    Funcionamiento:
    - Pide las variables de edad, dias y tipo para calcular el costo en la función principal.
    Entradas:
    - N/A
    Salidas:
    - Imprime la función auxiliar.
    """
    #Declaración de variables
    tipo=edad=dias=0
    edad=int(input("Ingrese la edad del paciente: "))
    dias=int(input("Ingrese la cantidad de días que estuvo hospitalizado: "))
    tipo=int(input("Ingrese el tipo de enfermedad del paciente: "))
    return print(calcularCostoAux(tipo,edad,dias))

#Programa principal
calcularCostoES()
#Fin del código

