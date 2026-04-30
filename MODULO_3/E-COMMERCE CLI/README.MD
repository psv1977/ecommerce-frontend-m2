# Sistema de Gestión Académica

Este proyecto implementa un modelo de clases en **Python** para la administración de una institución educativa, utilizando principios de **Programación Orientada a Objetos (POO)**.

## Descripción

El sistema permite gestionar la relación entre los distintos actores de un entorno académico: estudiantes, docentes, asignaturas y resultados. El diseño se centra en la arquitectura de datos y las relaciones de dependencia entre objetos.

## Arquitectura y Relaciones (UML)

El diseño del software se basa en los siguientes pilares de POO representados en el diagrama de clases:

* **Herencia:** Las clases `Alumno` y `Profesor` heredan de la clase base `Persona`, compartiendo atributos fundamentales como nombre y RUT.
* **Composición:** La clase `Alumno` tiene una relación de composición con `Calificacion`. Si el alumno es eliminado, sus registros académicos desaparecen.
* **Agregación:** El `Curso` agrupa a los `Alumnos`, permitiendo que ambos existan de forma independiente.
* **Asociación:** La `Asignatura` funciona como el punto de encuentro, asociando a un `Profesor` con múltiples `Alumnos`.

## Funcionalidades Principales

1.  **Gestión de Usuarios:** Registro de datos personales y académicos.
2.  **Inscripción Académica:** Capacidad de los alumnos para inscribirse en asignaturas.
3.  **Evaluación:** Registro de notas y cálculo automático de promedios por asignatura.
4.  **Organización Docente:** Asignación de especialidades y cátedras a profesores.


---
*Buena mar y mejor viento para este código.*