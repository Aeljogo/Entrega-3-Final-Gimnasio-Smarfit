

from models.Membresia import Membresia


class PlanSmart(Membresia):
    
    def __init__(self, fecha_inicio, fecha_fin, valor_base, sede):
        
        super().__init__(fecha_inicio, fecha_fin, valor_base)
        self.set_sede (sede)
        
    def get_sede(self):
        return self._sede
    
    def set_sede(self,sede):
        if sede !="":
            self._sede = sede
        else: 
            raise ValueError("La sede no puede estar vacía")
        
    def calcular_precio(self):
        return self.get_valor_base()
            
    def obtener_beneficios(self):    
        return (f"Acceso a la sede {self.get_sede()}, acceso a todas la áreas de la sede, Smartfit App y clases grupales con profesores")
    
    
    def mostrar_informacion(self):
            
         print("Fecha de inicio:", self.get_fecha_inicio())
         print("Fecha de fin:", self.get_fecha_fin())
         print("Valor base:", self.get_valor_base())
        
        
        
        
        
        
        