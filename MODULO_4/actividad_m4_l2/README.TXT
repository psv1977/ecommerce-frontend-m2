1. DESCRIPCIÓN GENERAL
----------------------
Este script implementa un sistema de modelado de libros utilizando 
Programación Orientada a Objetos pura en Python. El objetivo es 
demostrar la transición desde tipos de datos simples hacia 
estructuras de datos complejas y relacionadas.

2. ARQUITECTURA DE CLASES
-------------------------
A) Clase Autor:
   - Atributos: nombre, pais.
   - Rol: Entidad independiente que colabora con Libro.

B) Clase Editorial:
   - Atributos: nombre, ciudad.
   - Rol: Entidad compuesta, cuya vida depende del objeto Libro.

C) Clase Libro:
   - Atributos: titulo, anio_publicacion, autor (obj), editorial (obj).
   - Métodos clave:
     * __init__: Constructor de inicialización y composición.
     * mostrar_info(): Reporte consolidado de estado.
     * resumen(): Método polimórfico (simulación de sobrecarga).
     * get/set: Control de acceso a atributos sensibles.

3. HITOS TÉCNICOS DEMOSTRADOS
-----------------------------
[X] CONSTRUCTOR: Uso de __init__ y el puntero 'self'.
[X] ENCAPSULAMIENTO: Implementación de métodos accesadores y mutadores.
[X] SOBRECARGA: Lógica condicional con parámetros por defecto (texto=None).
[X] COLABORACIÓN: Inyección de un objeto 'Autor' en la clase 'Libro'.
[X] COMPOSICIÓN: Instanciación de 'Editorial' dentro del constructor de 'Libro'.


==============================================================