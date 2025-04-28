# Elaborado por: Xavier Céspedes Alvarado
# Fecha de creación: 12/03/2025 18:21
# Última modificación: 12/03/2025 19:24
# Versión de python: 3.13.2

#Definición de la función
def calcularSueldo(psueldoBase,pcategoria,phorasExtra):
    """
    Funcionamiento: La función calcula el salario final de una persona, tomando en cuenta sus horas extra y su categoría.
    Entradas:
    - psueldoBase: Es el sueldo base de la persona, sin incluir las horas extra.
    - pcategoria: Se refiere a la categoría a la que pertenece la persona.
    - phorasExtra: Son las horas extra trabajadas por la persona.
    Salidas:
    - psueldoBase + 30*costoHora(float): Es el sueldo de la persona con solo 30 horas extra, aunque trabajara más.
    - psueldoBase + phorasExtra*costoHora(float): Es el sueldo de la persona tomando en cuenta todas sus horas extra.
    """
    if pcategoria == 1:
        costoHora = 30
    elif pcategoria == 2:
        costoHora = 38
    elif pcategoria == 3:
        costoHora = 50
    elif pcategoria == 4:
        costoHora = 70
    else:                  #Aquí si la categoría es mayor a 4, el costo de la hora es 0
        costoHora = 0
    if phorasExtra>30:
        return psueldoBase + 30*costoHora
    else:
        return psueldoBase + phorasExtra*costoHora

#Código principal
sueldo= float(input("Ingrese su sueldo base: "))
categoria= int(input("Ingrese su categoría: "))
horasExtra= int(input("Ingrese las horas extra trabajadas: "))
print("Su sueldo final es de: " + str(calcularSueldo(sueldo,categoria,horasExtra)))
