

class GimnasioError(Exception):
    """Clase base para las excepciones del gimnasio."""
    pass

class EstudianteNoEncontradoError(GimnasioError):
    """Excepción lanzada cuando un estudiante no es encontrado en el gimnasio."""
    pass

class ClaseGrupalNoEncontradaError(GimnasioError):
    """Excepción lanzada cuando una clase grupal no es encontrada en el gimnasio."""
    pass

class EstudianteYaRegistradoError(GimnasioError):
    """Excepción lanzada cuando se intenta registrar un estudiante que ya está registrado en el gimnasio."""
    pass

class ClaseLlenaError(GimnasioError):
    """Excepción lanzada cuando se intenta agregar un estudiante a una clase grupal que ya está llena."""
    pass

class limiteInvitadosExcedido(GimnasioError):
    """Excepción lanzada cuando se excede el límite de invitados permitido por la membresía."""
    pass
