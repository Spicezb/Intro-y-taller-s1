# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 16/03/2025 20:03
# Última modificación: 17/03/2025 10:45
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
    return "El costo total del paciente fue de "+str(round(costo,2))+"."

def calcularCostoAux(ptipo,pedad,pdias):
    """
    Funcionamiento:
    - Determina si el tipo está entre 1 y 4, si los días son
    mínimo 1 y si la edad es mínimo 0.
    Entradas:
    - ptipo(int): Significa el tipo de enfermedad.
    - pedad(int): Es la edad del paciente.
    - pdias(int): Son los días que el paciente estuvo hospitalizado.
    Salidas:
    - "El tipo de enfermedad debe de estar entre 1 y 4"(str): Significa que el tipo de enfermedad no estuvo entre 1 y 4.
    - "La edad no puede ser menor a 0"(str): La edad ingresada fue menor a 0.
    - "La cantidad de días no puede ser menor a 1"(str): La cantidad de días ingresada fue menor a 1.
    - Llama a la función principal.
    """
    if ptipo < 1 or ptipo> 4:
        print("El tipo de enfermedad debe de estar entre 1 y 4.")
        return calcularCostoES()       #Se ejecuta la función de entrada y salida otra vez de manera automática
    elif pedad <= 0:
        print("La edad no puede ser menor a 0.")
        return calcularCostoES()
    elif pdias < 1:
        print("La cantidad de días no puede ser menor a 1.")
        return calcularCostoES()
    else:
        return calcularCosto(ptipo, pedad, pdias)

def calcularCostoES():
    """
    Funcionamiento:
    - Pide las variables de edad, días y tipo para calcular el costo en la función principal.
    Entradas:
    - N/A
    Salidas:
    - Imprime la función auxiliar.
    """
    #Declaración de variables
    while True:
        try:
            tipo=edad=dias=0
            edad=int(input("Ingrese la edad del paciente: "))
            dias=int(input("Ingrese la cantidad de días que estuvo hospitalizado: "))
            tipo=int(input("Ingrese el tipo de enfermedad:\nTipo 1)\nTipo 2)\nTipo 3\nTipo 4)\n"))
            return (calcularCostoAux(tipo,edad,dias))
        except ValueError:
            print("Debe ingresar solamente números enteros.")

#Programa principal
print(calcularCostoES())
#Fin del código