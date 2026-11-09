
from models.Entrenadores import Entrenadores
from models.Excepciones import ClaseLlenaError, EstudianteNoEncontradoError, EstudianteYaRegistradoError


class ClaseGrupal:

    def __init__(self, nombre, entrenador, cupo, horario):
        self.set_nombre(nombre)
        self.set_entrenador(entrenador)
        self.set_cupo(cupo)
        self.set_horario(horario)
        self._estudiantes = []

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        if nombre != "":
            self._nombre = nombre
        else:
            raise ValueError("El nombre no puede estar vacío")

    def get_entrenador(self):
        return self._entrenador

    def set_entrenador(self, entrenador):
        if isinstance(entrenador, Entrenadores):
            self._entrenador = entrenador
        else:
            raise ValueError("El entrenador debe ser un objeto de tipo Entrenadores")

    def get_cupo(self):
        return self._cupo

    def set_cupo(self, cupo):
        if cupo > 0:
            self._cupo = cupo
        else:
            raise ValueError("El cupo debe ser mayor a 0")

    def get_horario(self):
        return self._horario

    def set_horario(self, horario):
        if horario != "":
            self._horario = horario
        else:
            raise ValueError("El horario no puede estar vacío")

    def get_estudiantes(self):
        return self._estudiantes

    def agregar_estudiante(self, estudiante):
        if estudiante in self._estudiantes:
            raise EstudianteYaRegistradoError(
                f"{estudiante.get_nombre()} ya está inscrito en la clase '{self._nombre}'.")
        if len(self._estudiantes) >= self._cupo:
            raise ClaseLlenaError(f"La clase '{self._nombre}' está llena.")
        self._estudiantes.append(estudiante)

    def retirar_estudiante(self, estudiante):
        if estudiante not in self._estudiantes:
            raise EstudianteNoEncontradoError(
                f"{estudiante.get_nombre()} no está inscrito en la clase '{self._nombre}'.")
        self._estudiantes.remove(estudiante)

    def mostrar_informacion(self):
        print("Clase:", self._nombre)
        print("Horario:", self._horario)
        print(f"Cupo: {len(self._estudiantes)}/{self._cupo}")
        print("Entrenador:", self._entrenador.get_Nombre())
        for e in self._estudiantes:
            print(" -", e.get_nombre())
            
            
            
                