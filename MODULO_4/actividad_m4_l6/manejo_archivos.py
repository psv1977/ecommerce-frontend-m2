"""
1. Escribir en un archivo
• Crea un archivo llamado datos.txt desde Python (modo escritura).
• Escribe al menos 3 líneas de texto en él usando write().

"""

with open("datos.txt", "w", encoding="utf-8") as f:
    f.write("Línea 1\n")
    f.write("Línea 2\n")
    f.write("Línea 3\n")


"""
2.
Abre el archivo datos.txt en modo lectura y muestra su contenido en pantalla usando read().
"""

with open("datos.txt", "r", encoding="utf-8") as f:
    contenido = f.read()
    print(contenido)

"""
3.
Usa readline() para leer e imprimir solo la primera línea del archivo.
• Luego, usa un ciclo for para leer línea por línea el resto del archivo.
"""

with open("datos.txt", "r", encoding="utf-8") as f:
    primera_linea = f.readline()
    print(primera_linea)

    for linea in f:
        print(linea)

"""
4.
• Vuelve a abrir el archivo en modo append y agrega una línea nueva.
• Luego vuelve a abrirlo en modo lectura para comprobar que se agregó correctamente.
"""

with open("datos.txt", "a", encoding="utf-8") as f:
    f.write("Línea 4\n")

with open("datos.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea)

"""
5. 
Muestra por pantalla el nombre del archivo (.name), si está cerrado (.closed) y el modo de apertura
(.mode).
• Asegúrate de cerrar el archivo correctamente con .close() o usando with.
"""

with open("datos.txt", "r", encoding="utf-8") as f:
    print(f"Nombre: {f.name}")
    print(f"Modo: {f.mode}")
    print(f"¿Está cerrado dentro del with?: {f.closed}")

# Al salir del bloque 'with', el archivo se cierra automáticamente
print(f"¿Está cerrado fuera del with?: {f.closed}")