import os.path
import re

from EjSistemaGestionContactos.contacto import Contacto


class GestionContactos:
    NOMBRE_ARCHIVO = "contactos.txt"

    def __init__(self):
        self.lista_contactos = []
        self.cargar_contactos()

    def cargar_contactos(self):
        if not os.path.exists(self.NOMBRE_ARCHIVO):
            return
        try:
            with open(self.NOMBRE_ARCHIVO, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    nombre, telefono, email = linea.strip().split(";")
                    self.lista_contactos.append(Contacto(nombre, telefono, email))
        except Exception as e:
            print(f"Error al leer el archivo: {e}")

    def guardar_contactos(self):
        try:
            with open(self.NOMBRE_ARCHIVO, "w", encoding="utf-8") as archivo:
                for contacto in self.lista_contactos:
                    archivo.write(f"{contacto.nombre};{contacto.telefono};{contacto.email}\n")
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def validar_email(self, email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email)

    def agregar_contacto(self, nombre, telefono, email):
        if not self.validar_email(email):
            print("Formato de correo inválido")
            return
        self.lista_contactos.append(Contacto(nombre, telefono, email))
        self.guardar_contactos()
        print("Contacto guardado correctamente")

    def mostrar_contactos(self):
        if not self.lista_contactos:
            print("Lista de contactos vacía")
        else:
            for contacto in self.lista_contactos:
                print(contacto)

    def buscar_contacto(self, nombre):
        contactos_encontrados = [contacto for contacto in self.lista_contactos if contacto.nombre.lower() == nombre.lower()]
        if contactos_encontrados:
            for contacto in contactos_encontrados:
                print(contacto)
        else:
            print("Contacto no encontrado")

    def eliminar_contacto(self, nombre):
        longitud_lista_origianl = len(self.lista_contactos)
        self.lista_contactos = [contacto for contacto in self.lista_contactos if contacto.nombre.lower() != nombre.lower()]
        if len(self.lista_contactos) < longitud_lista_origianl:
            self.guardar_contactos()
            print("Contacto eliminado correctamente")
        else:
            print("Contacto no encontrado")