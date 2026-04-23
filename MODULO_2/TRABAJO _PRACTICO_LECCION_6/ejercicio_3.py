"""
Ejericio 3:Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga
cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos
a suponer que febrero tiene 28 días.
"""
meses = [
    ("Enero", 31),
    ("Febrero", 28),
    ("Marzo", 31),
    ("Abril", 30),
    ("Mayo", 31),
    ("Junio", 30),
    ("Julio", 31),
    ("Agosto", 31),
    ("Septiembre", 30),
    ("Octubre", 31),
    ("Noviembre", 30),
    ("Diciembre", 31)
]
while True:
    numero_mes = int(input("Ingrese un número de mes (1-12): "))
    
    if 1 <= numero_mes <= 12:
        nombre_mes, dias_mes = meses[numero_mes - 1]
        print(f"El mes de {nombre_mes} tiene {dias_mes} días.")
        break
    else:
        print("Número de mes no válido. Por favor ingrese un número entre 1 y 12.")
   

            