

from models.Excepciones import (EstudianteNoEncontradoError, ClaseGrupalNoEncontradaError, EstudianteYaRegistradoError)


class Gimnasio:
    def __init__(self, nombre, sede):
        
     self.set_nombre(nombre)
     self.set_sede(sede)
     self._estudiantes = []
     self._clases_grupales = []
    
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        if nombre !="":
            self._nombre=nombre
        else: 
            raise ValueError("El nombre no puede estar vacío")
        
    def get_sede(self):
        return self._sede
    
    def set_sede(self, sede):
        if sede !="":
            self._sede=sede
        else: 
            raise ValueError("La sede no puede estar vacía")
        
    def agregar_estudiante(self, estudiante):
        if estudiante in self._estudiantes:
            raise EstudianteYaRegistradoError(
                "El estudiante ya está registrado en el gimnasio"
            )
        self._estudiantes.append(estudiante)
      
       
        
    def buscar_estudiante(self, nombre):
        for estudiante in self._estudiantes:
            if estudiante.get_nombre() == nombre:
                return estudiante
        raise EstudianteNoEncontradoError(f"El estudiante con nombre '{nombre}' no fue encontrado en el gimnasio.")
    
    def agregar_clase_grupal(self, clase_grupal):
        if clase_grupal in self._clases_grupales:
            raise ValueError("La clase grupal ya está registrada en el gimnasio")
        self._clases_grupales.append(clase_grupal)        
        
    def mostrar_resumen(self):
        print(f"Nombre del gimnasio: {self._nombre}")
        print(f"Sede: {self._sede}")
        print("Estudiantes registrados:")
        for estudiante in self._estudiantes:
            print(f"- {estudiante.get_nombre()}")
        print("Clases grupales disponibles:")
        for clase in self._clases_grupales:
            print(f"- {clase.get_nombre()} (Entrenador: {clase.get_entrenador().get_Nombre()}, Cupo: {clase.get_cupo()}, Horario: {clase.get_horario()})")
            
            