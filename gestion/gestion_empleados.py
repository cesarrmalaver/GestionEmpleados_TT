from datos_empleados import Empleados, guardar_empleado, cargar_datos_empleados, eliminar_registro, modificar_registro
from Empleado import Empleado


def gestion_empleados():
    print("Gestion de empleados")
    while True:

        print('1. Agregar empleado.\n'
              '2. Eliminar empleado.\n'
              '3. Modificar empleado.\n'
              '4. Mostrar info de empleados\n'
              '5. Atras\n')

        opc = input('Digite la opción deseada: ')

        if opc == '1':
            agregar_empleados()
        elif opc == '2':
            eliminar_empleado()
        elif opc == '3':
            modificar_empleado()
        elif opc == '4':
            for empleado in Empleados:
                print(empleado)
        elif opc == '5':
            print("Saliendo...")
            break
        else:
            print("Opcion no valida intente nuevamente")

def gestion_areas():
    print("Gestion de areas")


def agregar_empleados():
    nombre = input("Digite el nombre del empleado: ")
    apellido = input("Digite el apellido del empleado: ")
    edad = input("Digite la edad: ")
    dni = input("Digite el documento de identificación: ")
    sexo = input("Digite el sexo: ")
    salario = input("Digite el salario: ")
    fecha_vinculacion = input("Digite la fecha de vinculacion: ")

    if len(Empleados) == 0:
        Empleados.append(Empleado(nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion))
        print('Empleado agregado')

    else:
        for empleado in Empleados:
            if empleado.dni == dni:
                print(f'Ya existe un empleado con DNI: {empleado.dni}')
                break
            else:
                Empleados.append(Empleado(nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion))
                print('Empleado agregado')
                break
    guardar_empleado(Empleados[-1])


def eliminar_empleado():
    global empleado

    if len(Empleados) == 0:
        print("No hay empleados creados")
    else:
        dni = int(input("Digite el DNI del empleado a eliminar: "))
        for empleado in Empleados:
            if int(empleado.dni) == dni:
                print(f'Se procede a eliminar el empleado: {empleado}')
                Empleados.remove(empleado)
                eliminar_registro(empleado)
                break

        else:
            print(f'El empleado con DNI {dni} no existe')

def modificar_empleado():
    if len(Empleados) == 0:
        print("No hay empleados creados")

    else:
        dni = input('Digite el DNI del empleado que quiere modificar: ')
        for empleado in Empleados:
            if int(empleado.dni) == int(dni):
                empleado.nombre = input("Digite el nombre del empleado: ")
                empleado.apellido = input("Digite el apellido del empleado: ")
                empleado.edad = input("Digite la edad: ")
                empleado.sexo = input("Digite el sexo: ")
                empleado.salario = input("Digite el salario: ")
                empleado.fecha_vinculacion = input("Digite la fecha de vinculacion: ")
                modificar_registro(empleado)
                print(f'Empleado con DNI {empleado.dni} modificado')
                break
        else:
            print(f'El empleado con DNI:{dni} NO existe')
