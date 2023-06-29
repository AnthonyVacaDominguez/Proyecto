from abc import ABC, abstractmethod

class Material(ABC):
    def __init__(self, codigo, autor, titulo, año, editorial, disponible, cantidad_disponible):
        self.codigo = codigo
        self.autor = autor
        self.titulo = titulo
        self.año = año
        self.editorial = editorial
        self.disponible = disponible
        self.cantidad_disponible = cantidad_disponible

    @abstractmethod
    def obtener_informacion(self):
        pass

class Libro(Material):
    def obtener_informacion(self):
        return f"Libro: {self.titulo} por {self.autor}"

class Revista(Material):
    def obtener_informacion(self):
        return f"Revista: {self.titulo} ({self.año})"

# Crear instancias de las clases hijas
libro1 = Libro("L001", "John Doe", "Libro de Prueba", "2023", "Editorial XYZ", True, 5)
revista1 = Revista("R001", "Jane Smith", "Revista de Prueba", "2023", "Editorial ABC", True, 10)

# Obtener información de las instancias
print(libro1.obtener_informacion())  # Imprime: Libro: Libro de Prueba por John Doe
print(revista1.obtener_informacion())  # Imprime: Revista: Revista de Prueba (2023)


# Demostración de ejecución de todas las clases
libro = Libro("L001", "John Doe", "Python Programming", 2022, "Tech Books", True, 5)
revista = Revista("R001", "Jane Smith", "Science Weekly", 2023, "Scientific Publishing", False, 0)
periodico = Periodico("P001", "David Johnson", "Daily News", 2023, "Media Corp", True, 10)

print("=== Información del Libro ===")
print(libro)
print("Tipo:", libro.obtener_tipo())
print()

print("=== Información de la Revista ===")
print(revista)
print("Tipo:", revista.obtener_tipo())
print()

print("=== Información del Periódico ===")
print(periodico)
print("Tipo:", periodico.obtener_tipo())

print('INTEGRANTES')
print('Goya Nuñez Valery Patricia Líder')
print('Hoyos Galarza Valeska Fiorella')
print('Contreras Campoverde Carolina Estefanía')
print('Vaca Dominguez Anthony Roger')