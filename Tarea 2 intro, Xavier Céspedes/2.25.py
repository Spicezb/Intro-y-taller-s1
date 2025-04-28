# Elaborado por: Xavier Céspedes Alvarado
# Fecha de creación: 11/03/2025 19:10
# Última modificación: 11/03/2025 20:27
# Versión de python: 3.13.2

#Definición de la función
def determinarMayor(pa, pb, pc):
    """
    Funcionamiento: La función determina cuál de tres números es el mayor, y si hay iguales selecciona dos o los tres como mayores.
    Entradas:
    - pa(float): Es el primer número.
    - pb(float): Es el segundo número.
    - pc(float): Es el tercer número.
    Salidas:
    - pa(float): pa es el mayor o es uno de los mayores en caso de que sean varios.
    - pb(float): pb es el mayor o es uno de los mayores en caso de que sean varios.
    - pc(float): pc es el mayor o es uno de los mayores en caso de que sean varios.
    """
    if pa>pb:
        if pa>pc: return pa
        else:
            if pa==pc: return pa  #solo se pone uno porque los dos son el mismo número
            else: return pc
    else:
        if pa==pb:
            if pa>pc: return pa
            else:
                if pa==pc: return pa  #solo se pone uno porque los tres son iguales
                else: return pc
        else:
            if pb>pc: return pb
            else:
                if pb==pc: return pb
                else: return pc           # Este es el caso donde pb>pa y pb<pc

#Código principal
a = float(input("Ingrese un primer número: "))
b = float(input("Ingrese un segundo número: "))
c = float(input("Ingrese un tercer número: "))
print(str(determinarMayor(a,b,c)) + " es el mayor")