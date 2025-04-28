# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 16/03/2025 9:22
# Última modificación: 17/03/2025 10:14
# Versión de python: 3.13.2

#Definición de funciones
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

def sumarDigitosMultiplosES():
    """
    Funcionamiento:
    - Comprueba que el número y el dígito sean enteros y mayores que 1.
    Entradas:
    - N/A
    Salidas:
    - "El número y el dígito deben ser enteros \n"(str): El número o el dígito no son enteros.
    - Llama a la función auxiliar.
    """
    while True:
        try:
            numero=digito=0
            numero=int(input("Ingrese un número: "))
            digito=int(input("Ingrese un digito del que quiera sumar los múltiplos en el número anterior: "))
            return sumarDigitosMultiplosAux(numero,digito)
        except ValueError:
            print("El número y el dígito deben ser enteros \n")

#Código principal
print(sumarDigitosMultiplosES())
#Fin del código