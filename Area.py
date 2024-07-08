class Area:
    def __init__(self, nombre, descripcion, lista_empleados_area):
        self._nombre = nombre
        self._descripcion = descripcion
        self._lista_empleados_area = lista_empleados_area

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, descripcion):
        self._descripcion = descripcion

    @property
    def lista_empleado_area(self):
        return self._lista_empleados_area

    @lista_empleado_area.setter
    def lista_empleado_area(self, lista_empleado_area):
        self._lista_empleados_area = lista_empleado_area

    def __str__(self):
        return f'Area: {self.nombre}, {self.descripcion}, {self.lista_empleado_area}'
