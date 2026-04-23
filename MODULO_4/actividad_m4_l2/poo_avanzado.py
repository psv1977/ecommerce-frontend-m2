"""
1. Definición de una clase con constructor
• Crea una clase Libro con los atributos titulo, autor y anio_publicacion.
• Define un método constructor __init__() que inicialice esos atributos.
• Crea un método mostrar_info() que imprima los datos del libro.
"""
class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
    
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de publicación: {self.anio_publicacion}")   
# Crear una instancia de la clase Libro
mi_libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
mi_libro2 = Libro("100 años de soledad", "Gabriel García Márquez", 1967)
mi_libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985)

# Llamar al método mostrar_info()
mi_libro1.mostrar_info()
mi_libro2.mostrar_info()
mi_libro3.mostrar_info()


"""
2. Métodos accesadores y mutadores
• Implementa métodos get_titulo() y set_titulo(nuevo_titulo) para acceder y modificar el
atributo titulo.
• Repite lo mismo para el atributo anio_publicacion.
• Usa estos métodos para modificar el título de un libro desde el programa principal.
"""

def get_titulo(self):
                return self.titulo

def set_titulo(self, nuevo_titulo):
                self.titulo = nuevo_titulo

def get_anio_publicacion(self):
                return self.anio_publicacion

def set_anio_publicacion(self, nuevo_anio):
                self.anio_publicacion = nuevo_anio


"""
3. Sobrecarga de métodos
• En la clase Libro, crea un método resumen() que:
• Si no recibe parámetros, imprime "Libro sin resumen disponible".
• Si recibe un texto como parámetro, imprime ese resumen.
• Simula la sobrecarga usando valores por defecto y condicionales en el método.
"""


def resumen(self, texto=None):
    if texto is None:
        print("Libro sin resumen disponible")
    else:
        print(f"Resumen: {texto}")
    # simulacion de sobrecarga usando valores por defecto y condicionales en el método resumen().


"""
4. Colaboración entre objetos
• Crea una clase Autor con atributos nombre y pais.
• Modifica la clase Libro para que el atributo autor sea un objeto de tipo Autor.
• En el método mostrar_info(), muestra también el nombre y país del autor.
"""
class Autor:
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais

class Libro:
    def __init__(self, titulo, autor, anio_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre}")
        print(f"País: {self.autor.pais}")
        print(f"Año de publicación: {self.anio_publicacion}")

# Crear una instancia de la clase Autor
autor1 = Autor("Gabriel García Márquez", "Colombia")

# Crear una instancia de la clase Libro
mi_libro = Libro("Cien años de soledad", autor1, 1967)

# Llamar al método mostrar_info()
mi_libro.mostrar_info()

"""
5. Composición
• Crea una clase Editorial con atributos nombre y ciudad.
• Modifica la clase Libro para que tenga un atributo editorial (objeto de tipo Editorial).
• Asegúrate de que la instancia de Editorial se cree dentro del constructor de Libro.
"""
class Editorial:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad

class Libro:
    def __init__(self, titulo, autor, anio_publicacion, nombre_editorial, ciudad_editorial):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.editorial = Editorial(nombre_editorial, ciudad_editorial)

    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor.nombre}")
        print(f"País: {self.autor.pais}")
        print(f"Año de publicación: {self.anio_publicacion}")
        print(f"Editorial: {self.editorial.nombre}")
        print(f"Ciudad: {self.editorial.ciudad}")
# Crear una instancia de la clase Autor
autor1 = Autor("Gabriel García Márquez", "Colombia")

# Crear una instancia de la clase Libro
mi_libro = Libro("Cien años de soledad", autor1, 1967, "Editorial Sudamericana", "Buenos Aires")

# Llamar al método mostrar_info()
mi_libro.mostrar_info() 