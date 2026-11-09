

class Entrenadores:
    
    def __init__(self, codigo, Nombre, Especialidad, Tipo_Entrenador):
        
        self.set_codigo(codigo)
        self.set_Nombre(Nombre)
        self.set_especialidad(Especialidad)
        self.set_Tipo_Entrenador(Tipo_Entrenador)
        
    def get_codigo(self):
        return self._codigo
    
    def set_codigo(self, codigo):
        if codigo !="":
            self._codigo=codigo
        else: 
            raise ValueError("El código no puede estar vacío")
        
    def get_Nombre(self):
        return self._Nombre   
    def set_Nombre(self, Nombre):
            if Nombre !="":
                self._Nombre=Nombre
            else: 
                raise ValueError("El Nombre no puede estar vacío") 

    def get_especialidad(self):
        return self._especialidad
    
    def set_especialidad(self, Especialidad):
        if Especialidad !="":
            self._especialidad=Especialidad
        else: 
            raise ValueError("La Especialidad no puede estar vacía")


    def get_Tipo_Entrenador(self):
        return self._tipo_Entrenador
    
    def set_Tipo_Entrenador(self, Tipo_Entrenador):
            if Tipo_Entrenador !="":
                self._tipo_Entrenador=Tipo_Entrenador
            else: 
                raise ValueError("El Tipo de Entrenador no puede estar vacío")
    
    
    def mostrar_informacion(self):
        print("Código:", self.get_codigo())
        print("Nombre:", self.get_Nombre())
        print("Especialidad:", self.get_especialidad())
        print("Tipo de Entrenador:", self.get_Tipo_Entrenador())
        
        