# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 16/03/2025 20:00
# Última modificación: 17/03/2025 09:41
# Versión de python: 3.13.2

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

def convertirDecimalES():
    """
    Funcionamiento:
    - Recibe el número que se va a convertir a decimal y llama la función auxiliar
    Entradas:
    - N/A
    Salidas:
    - Llama la función auxiliar
    """
    while True:
        try:
            numero=0
            numero=int(input("Ingrese un número binario para convertir a decimal: "))
            return convertirDecimalAux(numero)
        except ValueError:
            print("Debe ingresar un número entero \n")

print(convertirDecimalES())
