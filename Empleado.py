from Persona import Persona


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, dni, sexo, salario, fecha_vinculacion):
        super().__init__(nombre, apellido, edad, dni, sexo)
        self._salario = salario
        self._fecha_vinculacion = fecha_vinculacion

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, salario):
        self._salario = salario

    @property
    def fecha_vinculacion(self):
        return self._fecha_vinculacion

    @fecha_vinculacion.setter
    def fecha_vinculacion(self, fecha_vinculacion):
        self._fecha_vinculacion = fecha_vinculacion

    def __str__(self):
        return (f'Empleado: {super().__str__()}, salario:{self.salario}, '
                f'fecha vinculacion:{self.fecha_vinculacion}')