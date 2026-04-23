"""Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado
y la menor"""

notas = []
for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)

print("Notas ingresadas:")
for i, nota in enumerate(notas, ):
    print(f"Nota {i}: {nota}")

media = sum(notas) / len(notas)
print(f"Nota media: {media}")

max_nota = max(notas)
min_nota = min(notas)
print(f"Nota más alta: {max_nota}")
print(f"Nota más baja: {min_nota}")