"""
Ejercicio_1. Captura básica de errores
Escribe un programa que pida al usuario dividir dos números.
Utiliza try/except para capturar una división por cero y mostrar un mensaje de error amigable.
"""

def ejecutar_division():
    try:
        # Solicitamos los datos al usuario
        numerador = float(input("Ingresa el dividendo (número a dividir): "))
        denominador = float(input("Ingresa el divisor: "))
        
        # Realizamos la operación
        resultado = numerador / denominador
        print(f"Resultado: {numerador} / {denominador} = {resultado}")
        
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero. Por favor, intenta con un divisor distinto.")
    except ValueError:
        print("Error: Entrada no válida. Asegúrate de ingresar solo números.")

if __name__ == "__main__":
    ejecutar_division()



"""
2. Múltiples excepciones
• Agrega validación para que el usuario ingrese solo números.
Usa un bloque try/except con múltiples excepciones (ZeroDivisionError, ValueError).
"""

def ejecutar_division_multiple():
    
    try:
        # Solicitamos los datos
        entrada_1 = input("Ingresa el primer número (dividendo): ")
        entrada_2 = input("Ingresa el segundo número (divisor): ")

        # La conversión a float lanzará ValueError si la entrada no es numérica
        a = float(entrada_1)
        b = float(entrada_2)

        # Esta operación lanzará ZeroDivisionError si b es 0
        resultado = a / b

    except ValueError:
        print("Error: Tipo de dato no válido. Por favor, ingresa solo números (ej: 10 o 2.5).")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero. Intenta con un divisor diferente.")
    else:
        print(f"¡Operación exitosa! El resultado de {a} / {b} es: {resultado}")
    finally:
        print("Proceso de división finalizado.\n")

if __name__ == "__main__":
    ejecutar_division_multiple()


"""
3. Excepciones personalizadas
• Crea una función validar_edad(edad) que lance una excepción EdadInvalidaError si la edad
es menor que 0.
Define esta excepción como clase hija de Exception.
"""

class EdadInvalidaError(Exception):
    """Excepción personalizada para edades negativas."""
    pass

def validar_edad(edad):
    if edad < 0:
        raise EdadInvalidaError("La edad no puede ser un número negativo.")
    return True

def ejecutar_validacion_edad():
    print("--- Ejercicio 3: Excepciones Personalizadas ---")
    try:
        entrada = input("Por favor, ingresa tu edad: ")
        edad = int(entrada)
        validar_edad(edad)
        print(f"Edad validada correctamente: {edad} años.")
    except ValueError:
        print("Error: La edad debe ser un número entero.")
    except EdadInvalidaError as e:
        print(f"Error de validación: {e}")

if __name__ == "__main__":
    # Llamamos a la nueva función de prueba
    ejecutar_validacion_edad()

"""
4. Limpieza de recursos
• Simula la apertura de un archivo (puede ser un print("Abriendo archivo...")) y utiliza
finally para imprimir "Cerrando archivo..." aunque haya ocurrido un error.
"""

def demo_archivo_simulado():
    print("\n--- Ejercicio 4: Limpieza de Recursos (finally) ---")
    
    # Simulación de apertura de un recurso
    print("Abriendo archivo...")
    
    try:
        opcion = input("¿Deseas simular un error de lectura? (s/n): ").lower().strip()
        if opcion == "s":
            raise RuntimeError("Error de lectura: El archivo está corrupto o es ilegible.")
        print("Leyendo y procesando datos exitosamente...")
    except RuntimeError as e:
        print(f"Capturado: {e}")
    finally:
        # Este bloque se ejecuta SIEMPRE, haya error o no.
        print("Cerrando archivo... (Recurso liberado correctamente)")

if __name__ == "__main__":
    demo_archivo_simulado()
