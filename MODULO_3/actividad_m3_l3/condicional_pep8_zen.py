# ejercicio 1: desicion simple 
numero = int(input("Ingresa un numero: "))

if numero >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


# ejercicio 2: decision multiple con elif
calificacion = float(input("Ingresa tu calificación (entre 1 y 7): "))
if calificacion < 1 or calificacion > 7:
    print("Error: Calificación debe estar entre 1 y 7.")
elif calificacion == 7.0:
    print("¡Excelente!")
elif calificacion >= 6.0:
    print("Muy bien")
elif calificacion >= 5.0:
    print("Bien")
elif calificacion >= 4.0:
    print("Suficiente")
else:
    print("Insuficiente")

# ejercicio 3: condiciones anidadas
entero = int(input("Ingresa un número entero: "))
if entero >= 0:
    if entero > 0:
        print("numero positivo")
    else:
        print("es cero")
else:
    print("Numero negativo")


# ejercicio 4: condicion de borde
numero = int(input("Ingresa un número entre 0 y 100: "))

if (numero == 100) or (numero == 0):
    print("en el limite permitido")
elif (numero > 0) and (numero < 100):
    print("dentro del rango")
else:
    print("fuera del rango")