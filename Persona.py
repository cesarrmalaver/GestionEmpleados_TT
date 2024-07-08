class Persona:
    def __init__(self, nombre, apellido, edad, dni, sexo):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._dni = dni
        self._sexo = sexo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, sexo):
        self._sexo = sexo

    def __str__(self):
        return (f'Persona: {self.nombre} {self.apellido}, edad:{self.edad}, '
                f'dni:{self.dni}, sexo:{self.sexo}')

