
from datetime import date, timedelta

# Importación de las clases del proyecto
from models.Gimnasio import Gimnasio
from models.Alumno import Alumno
from models.Entrenadores import Entrenadores
from models.ClaseGrupal import ClaseGrupal

from models.PlanBlack import PlanBlack
from models.PlanFit import PlanFit
from models.PlanSmart import PlanSmart

from models.Excepciones import (
    EstudianteYaRegistradoError,
    ClaseLlenaError,
    EstudianteNoEncontradoError
)


if __name__ == "__main__":

    print("=" * 55)
    print("       SISTEMA DE GESTIÓN DEL GIMNASIO SMART FIT")
    print("=" * 55)

    # 1. CREACIÓN DEL GIMNASIO

    gimnasio_central = Gimnasio(
        "Smart Fit campanario",
        "Popayán"
    )

    print("\nGimnasio creado correctamente.")

    # 2. CREACIÓN DE ENTRENADORES

    entrenador1 = Entrenadores(
        "ENT001",
        "Andres Durán",
        "Musculación",
        "Tiempo completo"
    )

    entrenador2 = Entrenadores(
        "ENT002",
        "Santiago Martinez",
        "Entrenamiento funcional",
        "Medio tiempo"
    )

    print("\nEntrenadores creados correctamente.")

    # 3. CREACIÓN DE LAS MEMBRESÍAS

    fecha_inicio = date.today()
    fecha_fin = fecha_inicio + timedelta(days=30)

    membresia_black = PlanBlack(
        fecha_inicio,
        fecha_fin,
        100000,
        "Bogotá",
        5
    )

    membresia_fit = PlanFit(
        fecha_inicio,
        fecha_fin,
        70000,
        "Bogotá"
    )

    membresia_smart = PlanSmart(
        fecha_inicio,
        fecha_fin,
        80000,
        "Bogotá"
    )

    print("\nMembresías creadas correctamente.")

    # 4. CREACIÓN DE ALUMNOS

    alumno1 = Alumno(
        "Juan Díaz",
        "1020304050",
        22,
        membresia_black,
        75.0,
        1.75,
        "ganar masa muscular"
    )

    alumno2 = Alumno(
        "María López",
        "1020304051",
        21,
        membresia_fit,
        60.0,
        1.65,
        "perder peso"
    )

    alumno3 = Alumno(
        "Andrés Gómez",
        "1020304052",
        24,
        membresia_smart,
        80.0,
        1.80,
        "mejorar estado físico"
    )

    print("\nAlumnos creados correctamente.")

    # 5. REGISTRO DE ALUMNOS EN EL GIMNASIO

    gimnasio_central.agregar_estudiante(alumno1)
    gimnasio_central.agregar_estudiante(alumno2)
    gimnasio_central.agregar_estudiante(alumno3)

    print("\nAlumnos registrados correctamente.")

    # 6. CREACIÓN DE CLASES GRUPALES

    clase_funcional = ClaseGrupal(
        "Entrenamiento funcional",
        entrenador2,
        2,
        "Lunes y miércoles - 8:00 a. m."
    )

    clase_musculacion = ClaseGrupal(
        "Musculación guiada",
        entrenador1,
        3,
        "Martes y jueves - 10:00 a. m."
    )

    # Registro de clases en el gimnasio

    gimnasio_central.agregar_clase_grupal(clase_funcional)
    gimnasio_central.agregar_clase_grupal(clase_musculacion)

    print("\nClases grupales creadas correctamente.")

    # 7. INSCRIPCIÓN DE ALUMNOS EN CLASES GRUPALES

    clase_funcional.agregar_estudiante(alumno1)
    clase_funcional.agregar_estudiante(alumno2)

    clase_musculacion.agregar_estudiante(alumno1)
    clase_musculacion.agregar_estudiante(alumno3)

    print("\nAlumnos inscritos en las clases grupales.")

    # 8. RESUMEN GENERAL DEL GIMNASIO

    print("\n" + "=" * 55)
    print("                 RESUMEN GENERAL")
    print("=" * 55)

    gimnasio_central.mostrar_resumen()

    # 9. INFORMACIÓN DE LOS ALUMNOS

    print("\n" + "=" * 55)
    print("              INFORMACIÓN DE ALUMNOS")
    print("=" * 55)

    for alumno in gimnasio_central._estudiantes:
        print("\n")
        alumno.mostrar_informacion()

    # 10. POLIMORFISMO DE MEMBRESÍAS

    print("\n" + "=" * 55)
    print("          POLIMORFISMO DE MEMBRESÍAS")
    print("=" * 55)

    coleccion_membresias = [
        membresia_black,
        membresia_fit,
        membresia_smart
    ]

    # Se recorren objetos de diferentes clases hijas
    # utilizando los mismos métodos, sin condicionales.

    for membresia in coleccion_membresias:

        print("\nBeneficios:", membresia.obtener_beneficios())

        print(
            "Precio final: $",
            f"{membresia.calcular_precio():,.0f}"
        )

        print("¿Está vigente?:", membresia.esta_vigente())

    # 11. DEMOSTRACIÓN DE EXCEPCIONES PERSONALIZADAS

    print("\n" + "=" * 55)
    print("       DEMOSTRACIÓN DE EXCEPCIONES")
    print("=" * 55)

    # EXCEPCIÓN 1: Alumno ya registrado

    print("\nPrueba 1: Registro duplicado de un alumno.")

    try:
        gimnasio_central.agregar_estudiante(alumno1)

    except EstudianteYaRegistradoError as error:
        print("Excepción capturada:", error)

    # EXCEPCIÓN 2: Clase grupal llena

    print("\nPrueba 2: Intentar superar el cupo de una clase.")

    clase_prueba = ClaseGrupal(
        "Clase de prueba",
        entrenador1,
        1,
        "Viernes - 9:00 a. m."
    )

    # Se registra el primer alumno: ocupa el único cupo.

    clase_prueba.agregar_estudiante(alumno1)

    # Se intenta registrar un segundo alumno: se supera el cupo.

    try:
        clase_prueba.agregar_estudiante(alumno2)

    except ClaseLlenaError as error:
        print("Excepción capturada:", error)

    # EXCEPCIÓN 3: Alumno no inscrito en una clase

    print("\nPrueba 3: Retirar un alumno que no está inscrito.")

    try:
        clase_prueba.retirar_estudiante(alumno2)

    except EstudianteNoEncontradoError as error:
        print("Excepción capturada:", error)

    # 12. VERIFICACIÓN DE CONTINUIDAD DEL PROGRAMA

    print("\n" + "=" * 55)
    print("       SISTEMA EJECUTADO CORRECTAMENTE")
    print("=" * 55)

    print("Las pruebas finalizaron.")
    print("El programa continúa funcionando después de")
    print("capturar las excepciones personalizadas.")