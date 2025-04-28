# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 18/03/2025 10:38
# Última modificación: 18/03/2025 11:20
# Versión de python: 3.13.2

def esBinario(pnum):
    """
    Funcionamiento:
    - Mientras la variable pnum sea mayor que 0.
    - A la variable num se le asigna el residuo de la division de pnum entre 10.
    - Si algún residuo da mayor de 1, el número pasa a no ser binario automáticamente
    Entradas:
    -pnum(int): Contiene el número ingresado.
    Salidas:
    - True: El número es binario
    - False: El número no es binario
    """
    while pnum >0:                       # El ciclo se ejecuta mientras pnum sea mayor que 0.
        if pnum%10 > 1:                  # Y si el residuo es mayor de 1, el número no es binario automáticamente.
            return False
        pnum=pnum//10
    return True

def esBinarioAux(pnum):
    """
    Funcionamiento:
    -Se evalúa que el número no venga vacío.
    -Si no contuviese nada, se manda una excepción TypeError y lo devuelve a ingresar nuevamente el número.
    -Se cambia el tipo valor de la variable a int, para poder hacer la operación matematica.
    -Si ocurriese algún ValueError, salta la excepción y lo devuelve a ingresar nuevamente el número.
    Entradas:
    -pnum(str): Contiene el número ingresado.
    Salidas:
    -Se retorna lo que contiene la función esBinario.
    """
    try:
        if not pnum.strip():                        # Se prueba que el contenido no este vacio
            raise TypeError                         # Se crea el error TypeError en caso de que el contenido este vacío
        nume = int(pnum)
        if esBinario(nume)==True:
            return "El número es binario \n"
        else:
            return "El número no es binario \n"
    except TypeError:                               # Saltan las excepciones en caso de ser necesarias
        print("Debe ingresar un valor numérico \n")
        return esBinarioES()                        # Vuelve a hacer el proceso de ingresar el valor, hasta que esté correcto
    except ValueError:
        print("El valor debe ser únicamente entero \n")
        return esBinarioES()

def esBinarioES():
    """
    Funcionamiento:
    -Se pide que se ingrese un número para poder evaluarlo.
    Entradas:
    -N/A
    Salidas:
    -Se retorna lo que contiene la función esBinarioAux.
    """
    num = str
    num = input("Ingrese un número: ").strip()     # Se ingresa el número a evaluar, en string para luego hacerle validaciones
    return esBinarioAux(num)

print(esBinarioES())