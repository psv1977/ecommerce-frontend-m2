==================================================
MANEJO DE EXCEPCIONES EN PYTHON
==================================================

1. DESCRIPCIÓN
--------------
Este proyecto contiene una serie de ejercicios prácticos diseñados para 
dominar el control de errores y excepciones en Python. Se enfoca en mejorar 
la robustez de las aplicaciones mediante la anticipación de fallos comunes 
y la gestión controlada de los mismos.

2. CONTENIDO DEL SCRIPT (manejo_errores.py)
-------------------------------------------
El código se divide en cuatro secciones progresivas:

* EJERCICIO 1: Captura Básica
  - Implementación de bloques try/except.
  - Manejo de ZeroDivisionError para prevenir cierres inesperados.

* EJERCICIO 2: Múltiples Excepciones
  - Captura simultánea de ValueError (entradas no numéricas) y divisiones 
    por cero.
  - Uso del bloque 'else' para acciones que ocurren solo si no hay error.
  - Uso de 'finally' para ejecutar procesos de cierre.

* EJERCICIO 3: Excepciones Personalizadas
  - Creación de la clase 'EdadInvalidaError' (herencia de Exception).
  - Uso de la palabra clave 'raise' para lanzar errores lógicos propios.

* EJERCICIO 4: Limpieza de Recursos
  - Simulación de apertura y cierre de archivos.
  - Garantía de liberación de recursos mediante el bloque 'finally'.

