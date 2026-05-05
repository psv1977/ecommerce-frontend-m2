==================================================
SISTEMA DE GESTIÓN ACADÉMICA (POO)
==================================================

1. DESCRIPCIÓN DEL PROYECTO
---------------------------
Este proyecto es una implementación en Python que demuestra los pilares 
fundamentales de la Programación Orientada a Objetos (POO): Encapsulamiento, 
Herencia, Polimorfismo y Composición. Permite la gestión básica de personas, 
estudiantes, profesores y cursos.

2. ESTRUCTURA DE CLASES
-----------------------
* Persona: Clase base que gestiona datos básicos (RUT, nombre, edad) y 
  aplica encapsulamiento en el atributo _rut.
* Estudiante: Hereda de Persona. Incluye gestión de matrícula y un sistema 
  de calificaciones con soporte para ponderaciones.
* Profesor: Hereda de Persona. Especializada en la gestión de áreas de 
  expertiz docente.
* Curso: Clase de interacción que utiliza composición para agrupar a un 
  profesor titular y una lista de estudiantes matriculados.

3. FUNCIONALIDADES DESTACADAS
-----------------------------
* Polimorfismo: El método 'mostrar_rol' es sobrescrito por las clases hijas 
  para proporcionar un comportamiento específico según el tipo de objeto.
* Sobrecarga de Métodos: Implementada en 'agregar_calificacion' de la clase 
  Estudiante, permitiendo flexibilidad en el ingreso de notas.
* Relaciones entre Objetos: El sistema permite matricular estudiantes y 
  asignar docentes a cursos específicos de manera dinámica.

4. REQUISITOS DEL SISTEMA
-------------------------
* Lenguaje: Python 3.x
* Archivos incluidos:
    - POO2.py (Código fuente principal)
    - Diagrama_de_clases_POO2.png (Diagrama de clases)
    - poo2.puml (Diagrama de clases en formato UML)


5. INSTRUCCIONES DE EJECUCIÓN
-----------------------------
Para ejecutar el programa y ver la demostración en consola, utiliza:
    
    python POO2.py

6. DIAGRAMA DE CLASES
---------------------
El diseño de este sistema ha sido documentado mediante PlantUML para facilitar 
su comprensión arquitectónica.
