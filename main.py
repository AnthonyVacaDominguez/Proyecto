from docente import Docente
from estudiante import Estudiante
from libro import Libro
from revista import Revista

docente = Docente ("987654321", "Carolina", "Nuñez", "carolan@gmail.com", "0919255935", "Norte", "Ciencias")
estudiante = Estudiante("JaneSmith")

print("=== Información de la Persona ===")
print("Nombre:", docente.obtener_nombre())
print()

print("=== Información de la Persona ===")
print("Nombre:", 'obtener_nombre')
print()

libro = Material("L001", "John Doe", "Python Programming", 2022, "Tech Books", True, 5)
revista = Revista("R001", "Jane Smith", "Science Weekly")

pedido = Pedido( id = '987654321', solicitante = 'JaneSmith', lista_material = 'DESARROLLO EN PYTHON', fecha_prestamo ='10/Junio/2023', fecha_devolucion = '15/Junio/2023')
print(pedido1)

#INTEGRANTES
#Goya Nuñez Valery Patricia Líder
#Hoyos Galarza Valeska Fiorella
#Contreras Campoverde Carolina Estefanía
#Vaca Dominguez Anthony Roger
