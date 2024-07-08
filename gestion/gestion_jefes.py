from Empleado import Empleado
from Jefe import Jefe
from datos_empleados import Empleados

Jefes = []


def gestion_jefes():
    print("La funcionalidad de gestión de JEFES se encuentra en construccion")
    while True:
        print('1. Asignar empleado a Jefe.\n'
              '2. Mostrar la lista de empleados por Jefe\n'
              '3. Crear Jefe.\n'
              '4. Modificar Jefe\n'
              '5. Eliminar Jefe\n'
              '6. Atras\n')

        opc = input('Digite la opción deseada: ')

        if opc == '1':
            #asignar_jefe()
            pass
        elif opc == '2':
            # eliminar_jefe()
            pass
        elif opc == '3':
            crear_jefe()
            pass
        elif opc == '4':
            # for empleado in Empleados:
            #     print(empleado)
            pass
        elif opc == '6':
            print("Saliendo...")
            break
        else:
            print("Opcion no valida intente nuevamente")


def asignar_jef():
    jefe = input("Digite el DNI del Jefe")
    empleado = input("Digite el nombre del empleado")

    #Buscar al jefe


def asignar_jefe():
    dni_empleado = int(input("Digite el DNI del empleado a asignar: "))
    dni_jefe = int(input("Digite el DNI del Jefe a asignar: "))

    for jefe in Jefes:
        if int(jefe.dni) == dni_jefe:
            for empleado in Empleados:
                if int(empleado.dni) == dni_empleado:
                    jefe.agregar_empleado(empleado)
                    print(f"Empleado agregado")
                    break
                else:
                    print(f"No se encontró el empleado {dni_empleado}")
                    break
            break
        else:
            print(f"No se encontró el jefe {dni_jefe}")


def crear_jefe():
    nombre = input("Digite el nombre del jefe: ")
    apellido = input("Digite el apellido del empleado: ")
    edad = input("Digite la edad: ")
    dni = input("Digite el documento de identificación: ")
    sexo = input("Digite el sexo: ")
    salario = input("Digite el salario: ")
    fecha_vinculacion = input("Digite la fecha de vinculacion: ")

    if len(Jefes) == 0:
        Jefes.append(Jefe(nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion))
        print('Jefe agregado')
    else:
        for jefe in Jefes:
            if jefe.dni == dni:
                print(f'Ya existe un Jefe con DNI: {jefe.dni}')
                break
            else:
                Jefes.append(Jefe(nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion, []))
                print('Jefe agregado')
                break
