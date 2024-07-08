import csv

from Empleado import Empleado

nombre_archivo = 'datos/datos_empleados.csv'
Empleados = []


def cargar_datos_empleados():
    with open(nombre_archivo, newline='', encoding='utf-8') as f:
        datos = csv.reader(f, delimiter=',', quotechar=';')

        for r in datos:
            Empleados.append(Empleado(r[0], r[1], int(r[2]), int(r[3]), r[4], r[5], r[6]))
    print('Cargando info')
    return Empleados


def guardar_empleado(Empleado):
    file = open(nombre_archivo, "a+", encoding='utf-8')
    file.write(f'{Empleado.nombre},{Empleado.apellido},{Empleado.edad},'
               f'{Empleado.dni},{Empleado.sexo},{Empleado.salario},{Empleado.fecha_vinculacion}\n')
    file.close()
    print("Empleado guardado")
    pass


def eliminar_registro(Empleado):
    dni_a_borrar = int(Empleado.dni)
    with open(nombre_archivo, "r", encoding='utf-8') as f:
        data = list(csv.reader(f))
    f.close()

    with open(nombre_archivo, "w", newline="", encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in data:
            if int(row[3]) != dni_a_borrar:
                writer.writerow(row)
    f.close()


def modificar_registro(Empleado):
    dni_a_modificar = int(Empleado.dni)
    with open(nombre_archivo, "r", encoding='utf-8') as f:
        data = list(csv.reader(f))
    f.close()

    file = open(nombre_archivo, "w", encoding='utf-8')
    for row in data:
        if int(row[3]) != dni_a_modificar:
            file.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]},{row[6]}\n')
        elif int(row[3]) == dni_a_modificar:
            file.write(f'{Empleado.nombre},{Empleado.apellido},{Empleado.edad},'
                       f'{Empleado.dni},{Empleado.sexo},{Empleado.salario},{Empleado.fecha_vinculacion}\n')
    f.close()
