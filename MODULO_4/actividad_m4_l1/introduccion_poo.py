"""
PREGUNTA 1
Definición de POO
La Programación Orientada a Objetos (POO) es un paradigma de programación, es decir, 
un modelo o estilo de diseño de software que organiza el código alrededor de "datos" 
u objetos, en lugar de funciones y lógica pura.
"""
"""
# DIFERENCIAS PRINCIPALES:
# 1. Unidad básica: La Estructurada usa Funciones; la POO usa Objetos.
# 2. Datos: En la Estructurada están sueltos; en POO están protegidos dentro del objeto.
# 3. Pensamiento: Estructurada = "¿Qué pasos sigo?"; POO = "¿Quiénes interactúan?".
"""

"""
# =============================================================
# EJEMPLO DE OBJETO: LA CASA
# =============================================================

# ATRIBUTOS (Lo que la casa TIENE / Datos):
# - color = "Azul-Amarillo"
# - numero_habitaciones = 3
# - puerta_abierta = False

# MÉTODOS (Lo que la casa HACE / Acciones):
# - abrir_puerta(): Cambia el estado de la puerta a True.
# - pintar(nuevo_color): Cambia el atributo color.

# EN POO: La casa es un objeto autónomo que sabe su color y cómo abrirse.
# EN ESTRUCTURADA: Tendrías variables sueltas y funciones externas que las modifican.
# =============================================================
"""



"""
PREGUNTA 2
Definición de una clase simple
• Crea una clase llamada Perro.
• Agrega atributos como nombre, edad y raza.
• Define un método ladrar() que imprima "¡Guau!".
• Crea una instancia de la clase Perro y llama al método ladrar().
"""

class Perro:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
    
    def ladrar(self):
        print("¡Guau!")

# Crear una instancia de la clase Perro
mi_perro = Perro("Fido", 3, "Labrador")

# Llamar al método ladrar()
mi_perro.ladrar()   


"""
PREGUNTA 3
# ============================================================================
# GLOSARIO RÁPIDO DE POO (Paradigma Orientado a Objetos)
# ============================================================================

# 1. CLASE vs. OBJETO vs. INSTANCIA
# ----------------------------------------------------------------------------
# CLASE: Es el plano arquitectónico (el diseño). No es una casa real, sino el 
# esquema que dice cómo deben ser todas las casas de ese tipo.
#
# OBJETO: Es la casa física construida usando ese plano. Ocupa un lugar.
#
# INSTANCIA: Es el proceso de "construir" el objeto. Decimos que "mi_casa" 
# es una instancia de la clase "Casa".
# 


# 2. ATRIBUTO vs. ESTADO
# ----------------------------------------------------------------------------
# ATRIBUTO: Son las características definidas en el plano (variables).
# Ejemplo: color, numero_ventanas, esta_abierta.
#
# ESTADO: Es el valor actual de esos atributos en un momento determinado.
# Ejemplo: Si mi_casa.color es "Rojo" y puerta_abierta es "True", ese es su 
# ESTADO actual. Si la pinto de azul, su estado cambia.


# 3. MÉTODO vs. COMPORTAMIENTO
# ----------------------------------------------------------------------------
# MÉTODO: Es la función escrita en el código (la capacidad de hacer algo).
# Ejemplo: def abrir_puerta(self): ...
#
# COMPORTAMIENTO: Es la reacción del objeto cuando se ejecuta un método.
# Ejemplo: Cuando llamo a casa.abrir_puerta(), el comportamiento resultante 
# es que el ESTADO de 'puerta_abierta' cambia de False a True.
# 


# ============================================================================
# EJEMPLO EN CÓDIGO (RESUMEN):
# =============================================================
# class Casa:                 <-- CLASE (El plano)
#    def __init__(self):
#        self.color = "Verde" <-- ATRIBUTO (La característica)
#
# mi_hogar = Casa()           <-- INSTANCIA / OBJETO (La casa real)
# mi_hogar.color = "Azul"     <-- ESTADO (El valor actual del atributo)
"""

"""
PREGUNTA 4
Principios de POO
• Modifica la clase Perro para que los atributos estén encapsulados (prefijo _).
• Agrega un método mostrar_info() que devuelva el estado del objeto en forma de texto.
• Comenta brevemente qué significa la abstracción y cómo se relaciona con este ejemplo.
"""

class Perro:
    def __init__(self, nombre, edad, raza):
        self._nombre = nombre  # Atributo encapsulado
        self._edad = edad      # Atributo encapsulado
        self._raza = raza      # Atributo encapsulado
    
    def ladrar(self):
        print("¡Guau!")
    
    def mostrar_info(self):
        return f"Nombre: {self._nombre}, Edad: {self._edad}, Raza: {self._raza}"    
# Crear una instancia de la clase Perro
mi_perro = Perro("Cachupín", 3, "Kill-terrier")

# Llamar al método ladrar()
mi_perro.ladrar()

# Mostrar la información del perro
print(mi_perro.mostrar_info())  # Salida: Nombre: Fido, Edad: 3, Raza: Labrador 


