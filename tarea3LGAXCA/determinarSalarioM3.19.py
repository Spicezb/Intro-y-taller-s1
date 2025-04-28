# Elaborado por: Xavier Céspedes Alvarado y Luis Guillermo Alfaro Chacón
# Fecha de creación: 16/03/2025 20:00
# Última modificación: 17/03/2025 09:41
# Versión de python: 3.13.2

#Funciones-------------------------------------------------------------
def determinarMayor(pttlEmpleados):
    """
    Funcionamiento:
    -Se piden los datos de cada trabajador, y se calcula cuál de ellos tiene el
    salario más elevado.
    -Existe una validacion por si existiese un ValueError, salte la
    advertencia y no se caiga el programa.
    Entradas:
    -pttlEmpleados(int): Contiene el número de empleados.
    Salidas:
    -Se retorna el salario más elevado y el empleado que lo tiene.
    """
    while True:
        try:
            salarioMax=0
            empleadoMax=0
            conta = 1
            while conta <= pttlEmpleados:
                numEmpleado = int(input("Ingrese el ID del empleado "+str(conta)+": "))
                salario = int(input("Ingrese el salario del empleado "+str(numEmpleado)+": "))
                if salario > salarioMax:
                    salarioMax = salario
                    empleadoMax = numEmpleado  #El empleado con el salario más alto es remplazado con el nuevo id
                conta +=1
            return print("El salario más alto es de: "+str(salarioMax)+" y lo tiene el empleado con el ID: "+str(empleadoMax))
        except:
            print("Debe ingresar números enteros")
# ----------------------------------------------------------------------
def validarTtlEmpleados(pttlEmpleados):
    """
    Funcionamiento:
    -Se valida que el total de empleados de la empresa sea mayor que 0,
    si el valor fuera menor, se le dice al usuario que el dato debe ser mayor de 0
    y se vuelve a llamar a la función hasta que se ingrese bien el valor.
    Entradas:
    -pttlEmpleados(int): Contiene el número de empleados.
    Salidas:
    -Se retorna lo que contiene la función de
    """
    if pttlEmpleados <= 0:
        print("La cantidad de empleados debe ser mayor que 0...")
        determinarEmpleados()
    return determinarMayor(pttlEmpleados)
# ----------------------------------------------------------------------
def determinarEmpleados():
    """
    Funcionamiento:
    -Se ingresa el número total de empleados de la empresa.
    -Existe una validación, que si ocurre algún tipo de ValueError, salte la
    advertencia y no se caiga el programa.
    Entradas:
    -N/A
    Salidas:
    -Se retorna lo que contiene la función de validarTtlEmpleados
    """
    while True:
        try:
            ttlEmpleados=0
            ttlEmpleados=int(input("Ingrese el numero de empleados de la empresa: "))
            return validarTtlEmpleados(ttlEmpleados)
        except:
            print("Debe ingresar valores numéricos")

#Main----------------------------------------------------------------
determinarEmpleados()
#Fin del código