from gestion.gestion_empleados import *
from gestion.gestion_jefes import gestion_jefes

if __name__ == "__main__":
    while True:
        Empleados = cargar_datos_empleados()
        print('1. Gestión de empleados.\n'
              '2. Gestion de jefes.\n'
              '3. Gestion de areas.\n'
              '4. Salir\n')

        opc = input('Digite la opción deseada: ')

        if opc == '1':
            gestion_empleados()
        elif opc == '2':
            gestion_jefes()
        elif opc == '3':
            gestion_areas()
        elif opc == '4':
            print("Saliendo del programa")
            break
        else:
            print("Opcion no valida intente nuevamente")
