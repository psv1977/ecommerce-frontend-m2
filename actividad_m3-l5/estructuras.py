"""
Ejercicio 1. Crear estructuras lista, tupla, set y diccionario con los siguientes datos: 
nombre, apellido, edad, ciudad de residencia. Luego imprimir cada una de las estructuras.
"""

#Lista
persona_lista = ["Juan", "Pérez", 30, "Madrid"]
print("Lista:", persona_lista)

#Tupla
persona_tupla = ("María", "García", 25, "Barcelona")
print("Tupla:", persona_tupla)


#Set    
persona_set = {"Carlos", "López", 35, "Sevilla"}
print("Set:", persona_set)

#Diccionario
persona_diccionario = {
    "nombre": "Patricio",
    "apellido": "Saavedra",
    "edad": 49,
    "ciudad": "Viña del Mar"
}   
print("Diccionario:", persona_diccionario)




"""
#Ejercicio 2. Acceder a elementos; imprmir el segundo elemento de la lista, 
imprimie una clave y su valor desde el diccionario y explicar por qué no 
puedo acceder por indice a un set.
"""

#Acceder al segundo elemento de la lista
    
print("Segundo elemento de la lista:", persona_lista[1])

#Acceder a una clave y su valor desde el diccionario
print   ("Clave 'nombre' y su valor en el diccionario:", persona_diccionario["nombre"])
"""
Explicar por qué no puedo acceder por índice a un set

No se puede acceder por índice a un set porque los sets son colecciones no ordenadas 
y no permiten duplicados. No tienen un orden específico, por lo que no se puede
garantizar que los elementos estén en una posición determinada. 

Por lo tanto, no se pueden acceder a través de índices como en las listas o tuplas."
"""





"""
Ejercicio 3. Contar e iterar; usar len)= para mostrar la cantidad de elementos en cada;
iterar sobre cada estructura usando un for y muestra cada elemento por pantalla
"""

# Contar la cantidad de elementos en cada estructura
print("Cantidad de elementos en la lista:", len(persona_lista))
print("Cantidad de elementos en la tupla    :", len(persona_tupla))
print("Cantidad de elementos en el set     :", len(persona_set))
print("Cantidad de elementos en el diccionario:", len(persona_diccionario)) 

# Iterar sobre cada estructura usando un for y mostrar cada elemento por pantalla
print("Elementos en la lista:")
for elemento in persona_lista:
        print(elemento)

print("Elementos en la tupla:")
for elemento in persona_tupla:
        print(elemento)

print("Elementos en el set:")
for elemento in persona_set:
        print(elemento)

print("Elementos en el diccionario:")
for clave, valor in persona_diccionario.items():
        print(f"{clave}: {valor}")





"""
Ejercicio 4. Modificar estructuras

"""
#Agrega un nuevo elemento a la lista y al conjunto
persona_lista.append("España")
persona_set.add("España")   
    
#Borra un elemento de la lista
persona_lista.remove("Madrid")
    
#Agrega una nueva clave al diccionario
persona_diccionario["pais"] = "España"

#Intenta modificar la tupla y comenta qué ocurre
"""
Las tuplas son inmutables, lo que significa que no se pueden modificar después de su creación.
Si intentamos modificar una tupla, como por ejemplo:
persona_tupla[0] = "Ana"
Esto generará un error de tipo 'TypeError: 'tuple' object does not support item assignment',
indicando que no se pueden asignar valores a los elementos de una tupla.
"""    
    
    
  
