class Persona:
    def __init__(self, rut, nombre, edad):
        self._rut = rut # Atributo protegido (Encapsulamiento)
        self.nombre = nombre # Atributo público
        self.edad = edad

    # POLIMORFISMO: Este método será sobrescrito por las clases hijas
    def mostrar_rol(self):
        return "Soy una persona genérica en el sistema."

    def __str__(self):
        return f"{self.nombre} (RUT: {self._rut}, Edad: {self.edad})"

# ==========================================
# 2. CLASES HIJAS (Herencia y Polimorfismo)
# ==========================================
class Estudiante(Persona):
    def __init__(self, rut, nombre, edad, matricula):
        super().__init__(rut, nombre, edad) # Llamada al constructor padre
        self.matricula = matricula
        self.calificaciones = []

    # POLIMORFISMO: Sobrescribimos el método de la clase padre
    def mostrar_rol(self):
        return f"Soy un ESTUDIANTE y mi matrícula es {self.matricula}."

    # SOBRECARGA DE MÉTODOS (Estilo Python)
    def agregar_calificacion(self, nota, ponderacion=1.0):
        if ponderacion == 1.0:
            print(f"[{self.nombre}] Nota {nota} agregada con ponderación normal.")
        else:
            print(f"[{self.nombre}] Nota {nota} agregada con ponderación de {int(ponderacion*100)}%")
        self.calificaciones.append((nota, ponderacion))


class Profesor(Persona):
    def __init__(self, rut, nombre, edad, especialidad):
        super().__init__(rut, nombre, edad)
        self.especialidad = especialidad

    # POLIMORFISMO: Sobrescribimos el método de la clase padre
    def mostrar_rol(self):
        return f"Soy un PROFESOR y mi especialidad es {self.especialidad}."


# ==========================================
# 3. CLASE DE INTERACCIÓN (Composición)
# ==========================================
class Curso:
    def __init__(self, nombre_curso, codigo):
        self.nombre_curso = nombre_curso
        self.codigo = codigo
        self.profesor_titular = None 
        self.lista_estudiantes = [] 

    def asignar_profesor(self, profesor):
        self.profesor_titular = profesor
        print(f"Profesor {profesor.nombre} asignado al curso {self.nombre_curso}.")

    def matricular_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} matriculado en {self.nombre_curso}.")

    def mostrar_informacion_curso(self):
        print(f"\n--- INFORMACIÓN DEL CURSO: {self.nombre_curso} ({self.codigo}) ---")
        if self.profesor_titular:
            print(f"Docente a cargo: {self.profesor_titular.nombre} ({self.profesor_titular.especialidad})")

        print("Estudiantes matriculados:")
        for est in self.lista_estudiantes:
            print(f" - {est.nombre} (Matrícula: {est.matricula})")
        print("--------------------------------------------------\n")


# ==========================================
# 4. BLOQUE PRINCIPAL (Ejecución del Programa)
# ==========================================
if __name__ == "__main__":
    # A. INSTANCIAR OBJETOS
    profesor1 = Profesor("12345678-9", "Anakin Skywalker", 45, "Ciencias de la Fuerza")
    estudiante1 = Estudiante("20111222-3", "Anakin Skywalker", 22, "MAT-001")
    estudiante2 = Estudiante("21333444-5", "Obi-Wan Kenobi", 24, "MAT-002")
    curso_poo = Curso("Programación Orientada a Objetos", "INF-101")

    # B. POLIMORFISMO EN ACCIÓN
    print("--- DEMOSTRACIÓN DE POLIMORFISMO ---")
    personas = [profesor1, estudiante1]
    for persona in personas:
        print(persona.mostrar_rol())
    print()

    # C. SOBRECARGA DE MÉTODOS EN ACCIÓN
    print("--- DEMOSTRACIÓN DE SOBRECARGA (Estilo Python) ---")
    estudiante1.agregar_calificacion(6.5)
    estudiante1.agregar_calificacion(7.0, 0.4)
    print()

    # D. INTERACCIÓN ENTRE OBJETOS
    print("--- DEMOSTRACIÓN DE INTERACCIÓN ENTRE OBJETOS ---")
    curso_poo.asignar_profesor(profesor1)
    curso_poo.matricular_estudiante(estudiante1)
    curso_poo.matricular_estudiante(estudiante2)

    curso_poo.mostrar_informacion_curso()