class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return (f"Nombre: {self.nombre} Telefono: {self.telefono} Email: {self.email}")