

from abc import ABC, abstractmethod
from datetime import date

class Membresia(ABC):
    def __init__(self, fecha_inicio, fecha_fin, valor_base):
        self.set_fecha_inicio(fecha_inicio)
        self.set_fecha_fin(fecha_fin)
        self.set_valor_base(valor_base)
     
    def get_fecha_inicio(self):  
        return self.fecha_inicio
    
    def set_fecha_inicio(self, fecha_inicio):
        if isinstance(fecha_inicio, date):
            self.fecha_inicio = fecha_inicio
        else:
            raise ValueError("La fecha de inicio debe ser un objeto de tipo date")
    
    def get_fecha_fin(self):
        return self.fecha_fin
    
    def set_fecha_fin(self, fecha_fin):
        if isinstance(fecha_fin, date):
            self.fecha_fin = fecha_fin
        else:
            raise ValueError("La fecha de fin debe ser un objeto de tipo date")
        
    def get_valor_base(self):
        return self.valor_base
    
    def set_valor_base(self, valor_base):
        if valor_base > 0:
            self.valor_base = valor_base
        else:
            raise ValueError("El valor base debe ser mayor a 0")
             
    @abstractmethod
    def calcular_precio(self):
        pass    
        
        

    @abstractmethod
    def obtener_beneficios(self):
        pass 
    def esta_vigente(self):
        hoy = date.today()
        return self.fecha_inicio <= hoy <= self.fecha_fin

    def mostrar_informacion(self):
        
     print("Fecha de inicio:", self.get_fecha_inicio())
     print("Fecha de fin:", self.get_fecha_fin())
     print("Valor base:", self.get_valor_base())
        
        
    
    
    
    