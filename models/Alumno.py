

from models.Membresia import Membresia
from models.EstructuraFisica import EstructuraFisica

class Alumno:
    
    def __init__(self, nombre, documento, edad, membresia, peso, estatura, objetivo):
        self.set_nombre(nombre)
        self.set_documento(documento)
        self.set_edad(edad)
        self.set_Membresia(membresia)
       
        self.estructura_fisica = EstructuraFisica(peso, estatura, objetivo)
        
    def get_documento(self):
        return self._documento
    
    def set_documento(self, documento):
        if documento !="":
            self._documento=documento
        else: 
            raise ValueError("El documento no puede estar vacío")
        
    def get_nombre(self):
        return self._nombre 
    
    def set_nombre(self, nombre):
        if nombre !="":
            self._nombre=nombre
        else: 
            raise ValueError("El nombre no puede estar vacío")     
        
    def get_edad(self):
        return self._edad
    def set_edad(self,edad):
        if edad > 0:
            self._edad=edad
        else: 
            raise ValueError("La edad debe ser mayor a 0")
    
    
    
    def get_Membresia(self):
        return self._membresia
    
    def set_Membresia(self, membresia): 
        if isinstance(membresia, Membresia):
            self._membresia = membresia
            
        else:
            raise ValueError("El estudiante debe tener una membresía para ingresar")
        
    def get_Estructura_fisica(self):
        return self.estructura_fisica
    
    
    
    def mostrar_informacion(self):
        print("Nombre:", self.get_nombre())
        print("Documento:", self.get_documento())
        print("Edad:", self.get_edad())
        self.get_Membresia().mostrar_informacion()
        self.get_Estructura_fisica().mostrar_informacion()
        
        
            