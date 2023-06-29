from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, cedula, nombre, apellido, email, telefono, direccion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.numero_libros = 0
        self.activo = True

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Cedula: {self.cedula}"

    @property
    @abstractmethod
    def pedir_libro(self):
        pass

    @property
    @abstractmethod
    def devolver_libro(self):
        pass

#INTEGRANTES
#Goya Nuñez Valery Patricia Líder
#Hoyos Galarza Valeska Fiorella
#Contreras Campoverde Carolina Estefanía
#Vaca Dominguez Anthony Roger

