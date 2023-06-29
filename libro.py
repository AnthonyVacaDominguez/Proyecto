from Material import Material
class Libro:
    def __init__(self, id, tipo_pasta):
        self._id = id
        self._tipo_pasta = tipo_pasta
        self._contador_libro = 0
        self._disponible = True

    def get_id(self):
        return self._id

    def set_id(self, new_id):
        self._id = new_id

    def get_tipo_pasta(self):
        return self._tipo_pasta

    def set_tipo_pasta(self, new_tipo_pasta):
        self._tipo_pasta = new_tipo_pasta

    def get_contador_libro(self):
        return self._contador_libro

    def set_contador_libro(self, new_contador_libro):
        self._contador_libro = new_contador_libro

    def actualizar_disponibilidad(self, disponible):
        self._disponible = disponible


libro1 = Libro(1, "Tapa dura")
libro2 = Libro(2, "Tapa blanda")


libro1.set_id(3)
libro1.set_tipo_pasta("Tapa flexible")
libro1.set_contador_libro(5)
libro1.actualizar_disponibilidad(False)


print(libro1.get_id()) 
print(libro1.get_tipo_pasta())  
print(libro1.get_contador_libro())  
print(libro1._disponible)  

#INTEGRANTES
#Goya Nuñez Valery Patricia Líder
#Hoyos Galarza Valeska Fiorella
#Contreras Campoverde Carolina Estefanía
#Vaca Dominguez Anthony Roger
