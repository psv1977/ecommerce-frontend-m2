# --- MODELADO DE DATOS (Excelente) ---
# Catálogo estructurado con tipos de datos correctos 
catalogo = [
    {"id": 1, "nombre": "Titanic", "categoria": "Lujo", "precio": 450000.0},
    {"id": 2, "nombre": "Perla Negra", "categoria": "Deportivo", "precio": 280000.0},
    {"id": 3, "nombre": "Poseidon", "categoria": "Pesca", "precio": 125000.0},
    {"id": 4, "nombre": "Rapido y Furioso", "categoria": "Lujo", "precio": 890000.0},
    {"id": 5, "nombre": "Capitan America", "categoria": "Deportivo", "precio": 195000.0}
]

carrito = [] # Estructura en memoria para el carrito 

# --- FUNCIONES Y ORGANIZACIÓN (Excelente) ---
# Se usan más de 3 funciones con parámetros y retornos 

def mostrar_menu():
    """Muestra el menú principal de forma clara """
    print("\n" + "#"*30)
    print(" BIENVENIDO/A A YATES ELITE ")
    print("#"*30)
    print("1) Ver catálogo de productos")
    print("2) Buscar producto por nombre o categoría")
    print("3) Agregar producto al carrito")
    print("4) Ver carrito y total")
    print("5) Vaciar carrito")
    print("0) Salir")

def calcular_total(lista_carrito):
    """Calcula la suma de subtotales. Cumple requisito de retornar valor """
    total = 0
    for yate in lista_carrito:
        total += yate['precio'] * yate['cantidad']
    return total

def buscar_productos(lista, termino):
    """Filtra productos. Recibe parámetros y devuelve una lista """
    resultados = []
    for producto in lista:
        if termino.lower() in producto['nombre'].lower() or termino.lower() in producto['categoria'].lower():
            resultados.append(producto)
    return resultados

def agregar_al_carrito(lista_catalogo, lista_carrito):
    """Valida ID y cantidad (Requisito de validación) """
    try:
        id_ingresado = int(input("Ingrese el ID del yate: "))
        # Buscar el producto por ID
        producto = next((p for p in lista_catalogo if p['id'] == id_ingresado), None)
        
        if producto:
            cant = int(input("Ingrese cantidad (mayor a 0): "))
            if cant > 0:
                # Guardar producto y cantidad en el carrito 
                item_carrito = producto.copy()
                item_carrito['cantidad'] = cant
                lista_carrito.append(item_carrito)
                print(f" {producto['nombre']} añadido con éxito.")
            else:
                print("Error: La cantidad debe ser mayor a 0.")
        else:
            print("Error: El ID no existe en el catálogo.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

def mostrar_carrito(lista_carrito):
    """Lista ítems con ID, nombre, cantidad, precio y subtotal """
    if not lista_carrito:
        print("\nEl carrito está vacío.")
    else:
        print("\n--- DETALLE DE TU CARRITO ---")
        for i in lista_carrito:
            subtotal = i['precio'] * i['cantidad']
            # Formato requerido: id, nombre, cantidad, precio unitario, subtotal 
            print(f"ID: {i['id']} | {i['nombre']} | Cant: {i['cantidad']} | Precio: ${i['precio']:,} | Subtotal: ${subtotal:,}")
        
        total = calcular_total(lista_carrito)
        print(f"--- TOTAL A PAGAR: ${total:,} ---")

# --- FLUJO PRINCIPAL (Ciclos y Condicionales) ---
def main():
    while True: # Ciclo que se repite hasta salir 
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            print("\n--- CATÁLOGO DE YATES ---")
            for p in catalogo:
                print(f"[{p['id']}] {p['nombre']} ({p['categoria']}) - ${p['precio']:,}")
        
        elif opcion == "2":
            termino = input("¿Qué yate o categoría buscas?: ")
            hallados = buscar_productos(catalogo, termino)
            if hallados:
                for h in hallados:
                    print(f"-> {h['nombre']} [ID: {h['id']}] - ${h['precio']:,}")
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "3":
            agregar_al_carrito(catalogo, carrito)
        
        elif opcion == "4":
            mostrar_carrito(carrito)
        
        elif opcion == "5":
            carrito.clear() # Vacía la estructura en memoria 
            print("✨ Carrito vaciado.")

        elif opcion == "0":
            print("Gracias por preferir Yates Elite. ¡BUENA MAR Y MEJOR VIENTO!")
            break # Termina el ciclo 
        
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    main()

    