from Empleado import Empleado


class Jefe(Empleado):
    def __init__(self, nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion)
        self._lista_empleados = []

    @property
    def empleados_a_cargo(self):
        return self._lista_empleados

    # @empleados_a_cargo.setter
    # def empleados_a_cargo(self, empleados_a_cargo):
    #     self._empleados_a_cargo = empleados_a_cargo

    def agregar_empleado(self, empleado):
        self._lista_empleados.append(empleado)

    def listar_empleados_a_cargo(self):
        for empleado in self._lista_empleados:
            print(empleado.__str__())

    def __str__(self):
        return f'Jefe: {super().__str__()}'
