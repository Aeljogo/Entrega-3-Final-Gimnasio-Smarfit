

class EstructuraFisica:
    def __init__(self, peso, altura, objetivo):
        
        self.set_peso(peso)
        self.set_altura(altura)
        self.set_objetivo(objetivo)
        
    def get_peso(self):
        return self._peso
    
    def set_peso(self,peso):
        if peso > 0.0:
            self._peso =peso
            
        else:
            raise ValueError("El peso debe ser mayor a 0.0")
            
            

    def get_altura(self):
        return self._altura
        
    def set_altura(self,altura):
        if altura > 0.0:
            self._altura = altura
            
        else:
            raise ValueError("La estatura debe ser mayor a 0.0")
            
                
    def get_objetivo(self):
        return self._objetivo
    
    def set_objetivo(self, objetivo):
        if objetivo == "perder peso" or objetivo == "ganar masa muscular" or objetivo == "mejorar estado físico":
            self._objetivo = objetivo
        else:
            raise ValueError("El objetivo debe ser perder peso, ganar masa muscular o mejorar estado físico, debe haber un objetivo por el cual el usuario quiera asistir al gimnasio")
    
    
    def calcular_IMC(self):
        imc = self._peso / (self._altura ** 2)
        return imc
    def mostrar_informacion(self):
        print("Peso:", self.get_peso(), "Kg")
        print("Altura:", self.get_altura(), "m")
        print("Objetivo:", self.get_objetivo())
        print("IMC:", self.calcular_IMC())
        
        