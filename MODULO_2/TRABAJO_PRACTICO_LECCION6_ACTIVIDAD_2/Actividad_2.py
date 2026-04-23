""""
este progra debe ingreas las notas de los alumno, se pregunta cuantos datos se van a ingresar, luego se ingresan las notas una a una, finalmente
como salida cuantas notas ingresadas son mayores que el promedio 

"""

dato=[]
cantidad=int(input("¿cuántos datos ingresará?: "))
for i in range(cantidad):
    nota=float(input(f"Ingrese la nota {i+1}: "))
    dato.append(nota)

promedio=sum(dato)/len(dato)
contador=0
for nota in dato:
    if nota>promedio:
        contador+=1
print(f" {contador} datos son mayores que el promedio")

