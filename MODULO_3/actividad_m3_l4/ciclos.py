# ejercicio 1. Uso básico de while

contador = 0

while contador < 5:
    print("Contador:", contador)
    contador += 1
print("¡Listo! El contador ha alcanzado 5.")

# ejercicio 2. Uso básico de for

frutas = ["manzana", "plátano", "naranja"]
for fruta in frutas:
    print("Fruta:", fruta)
print("¡Listo! Se ha recorrido toda la lista que contiene las frutas.")

# ejercicio 3. Condición de un ciclo
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 == 0:
        print("Número par:", numero)
    else:
        print("Número impar:", numero)

# ejercicio 4. Ciclo infinito controlado con break
while True:
    entrada = input("Introduce un número (o '0' para salir): ")
    if entrada == '0' or entrada.lower() == 'break':
        break
    print("Has introducido:", entrada)
print("¡Listo! Se ha terminado el ciclo.")

#ejercicio 5. Ciclo anidado (que imprima una tabla de multiplicar del 1 al 3)
for i in range(1, 4):
    print(f"Tabla del {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")   
        print()


#ejercicio 6. Uso del continue (recorre una lista de nombres. Si es Juan, lo omite usando continue e imprime el resto de los nombres)
nombres = ["Ana", "Juan", "Pedro", "María", "Juan", "Luis"]
for nombre in nombres:
    if nombre == "Juan":
        continue
    print("Nombre:", nombre)


