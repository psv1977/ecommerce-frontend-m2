"""
En este ejercicio se ingresa un numero par cualquiera del 2 al 100 y se imprimen todos los pares siguientes a ese numero, hasta el 100.
Si se ingresa un numero impar, desde el 1 al 99 se imprima en paantalla todos los impares siguientes a ese numero, hasta el 99.
Si se ingreesa el 0 o un numero menor y si ingreso un numero mayor al 100 el programa envia un mensdsaje que no es posible y se vuelve a pedir el numero.
"""

while True:
    numero = int(input("Ingrese un numero par del 2 al 100 o un numero impar del 1 al 99: "))
    
    if numero < 0 or numero > 100:
        print("Numero no valido. Por favor ingrese un numero entre 0 y 100.")
        continue
    
    if numero % 2 == 0 and 2 <= numero <= 100:
        print(f"Numeros pares siguientes a {numero}:")
        for i in range(numero + 2, 101, 2):
            print(i)
        break
    elif numero % 2 != 0 and 1 <= numero <= 99:
        print(f"Numeros impares siguientes a {numero}:")
        for i in range(numero + 2, 100, 2):
            print(i)
        break
    else:
        print("No es posible realizar la operacion. Por favor ingrese un numero par del 2 al 100 o un numero impar del 1 al 99.")

