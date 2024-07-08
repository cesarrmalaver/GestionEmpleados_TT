from Empleado import Empleado
from Jefe import Jefe

empleado1 = Empleado('Ramiro','Raur',45,333,'m',888,'10/10/2021')
empleado2= Empleado('Ramona','Raur',45,333,'m',888,'10/10/2021')
jefe1 = Jefe("Oscar", "Ordoñez", 14, 1, 'M', 123, "19/05/2024")

#print(jefe1)

jefe1.agregar_empleado(empleado1)
jefe1.agregar_empleado(empleado2)
print(jefe1.listar_empleados_a_cargo())

#print(jefe1)


