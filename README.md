


Para este sistema quise implementar o poner en practica en un gimasnio, en este caso, smart fit que es donde entreno yo. 
Su propósito es representar y administrar diferentes procesos relacionados con el funcionamiento de un gimnasio, 
incluyendo el registro de alumnos, la asignación de membresías, la organización de entrenadores y la gestión de clases grupales.

La administración de un gimnasio requiere organizar información sobre sus estudiantes, los planes de membresía disponibles y las actividades grupales.
Cuando estos procesos no cuentan con mecanismos adecuados de control, pueden presentarse situaciones como registros duplicados, 
inscripciones en clases sin disponibilidad y dificultades para administrar los alumnos inscritos.

Así se ve la composición del sistema
main.py	Programa  principal que ejecuta los escenarios de funcionamiento.
models/Membresia.py	 Clase abstracta que establece las características generales de las membresías.
models/PlanFit.py	 Clase que representa el plan Fit.
models/PlanSmart.py	 Clase que representa el plan Smart.
models/PlanBlack.py	 Clase que representa el plan Black.
models/Alumno.py	 Administra la información de los alumnos y sus membresías.
models/EstructuraFisica.py	Gestiona características físicas y permite calcular el IMC.
models/Entrenadores.py	Representa a los entrenadores.
models/ClaseGrupal.py	Gestiona las clases grupales, los cupos y las inscripciones.
models/Gimnasio.py	Administra los registros de estudiantes y clases.
models/Excepciones.py	Contiene las excepciones personalizadas.

Estos son los pasos para la ejecución: 
Para ejecutar el programa se deben seguir los siguientes pasos:
1.	Descargar o clonar el repositorio desde GitHub.
2.	Abrir la carpeta del proyecto.
3.	Verificar que se encuentre el archivo principal main.py.
4. ejecutar el main en el visual studio

Tomé tres excepciones que son: 
EstudianteYaRegistradoError
Se produce cuando se intenta registrar un estudiante que ya existe en el sistema.
ClaseLlenaError
Se genera cuando se intenta inscribir a un alumno en una clase que ha alcanzado su capacidad máxima.
EstudianteNoEncontradoError
Se presenta cuando se intenta retirar de una clase a un estudiante que no se encuentra inscrito.
Estas excepciones permiten mostrar mensajes claros y continuar con la ejecución del programa.
