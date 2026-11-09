

from models.Membresia import Membresia

from models.Excepciones import limiteInvitadosExcedido 

class PlanBlack(Membresia):
    
    def __init__(self, fecha_inicio, fecha_fin, valor_base, sede, limite_invitados):
        
        super().__init__(fecha_inicio, fecha_fin, valor_base)
        self.set_sede(sede)
        self.set_limite_invitados(limite_invitados)
        
    def get_sede(self):
        return self._sede
    
    def set_sede(self,sede):
        if sede !="":
            self._sede = sede
        else: 
            raise ValueError("La sede no puede estar vacía")
            
    def get_limite_invitados(self):
        return self._limite_invitados
    
    def set_limite_invitados(self, limite_invitados):
        if limite_invitados > 0:
            self._limite_invitados = limite_invitados
        else:
            raise ValueError("El límite de invitados debe ser mayor a 0")
            
    def calcular_precio(self):
        return self.get_valor_base() * 1.5
    
    def obtener_beneficios(self):    
        return f"Acceso a la sede {self.get_sede()}, acceso a todas la áreas de la sede, Smartfit App y clases grupales con profesores, acceso a invitados hasta un máximo de {self.get_limite_invitados()} invitados"
    
    
    def mostrar_informacion(self):
            
         print("Fecha de inicio:", self.get_fecha_inicio())
         print("Fecha de fin:", self.get_fecha_fin())
         print("Valor base:", self.get_valor_base())
        
        
