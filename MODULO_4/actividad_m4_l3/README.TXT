=========================================
      SISTEMA ACADÉMICO - README
=========================================

RESUMEN:
Modelo en Python para gestionar la relación entre
alumnos, profesores y sus notas.

ESTRUCTURA:
- Persona: Clase base (Nombre, RUT).
- Alumno / Profesor: Heredan de Persona.
- Asignatura: Une al profesor con sus alumnos.
- Calificación: Calcula promedios (vinculada al Alumno).

RELACIONES:
- Herencia: Alumno y Profesor son Personas.
- Composición: Las notas dependen del Alumno.
- Agregación: Los alumnos integran Cursos.

