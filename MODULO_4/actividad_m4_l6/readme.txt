## ¿Qué diferencia notaste entre write() y append()?
La diferencia principal radica en el tratamiento del contenido existente:
- El modo escritura ('w') sobrescribe el archivo por completo. Si el archivo ya existía, se borra su contenido previo.
- El modo append ('a') preserva el contenido existente y añade la nueva información al final del archivo.

## ¿Qué ventaja tiene usar 'with open(...)' frente a abrir y cerrar manualmente?
- Gestión Automática: 'with' cierra el archivo automáticamente al finalizar el bloque, incluso si ocurre una excepción.
- Seguridad: Evita fugas de memoria y bloqueos de archivos en el sistema operativo.
- Código Limpio: No es necesario recordar llamar a .close() explícitamente.