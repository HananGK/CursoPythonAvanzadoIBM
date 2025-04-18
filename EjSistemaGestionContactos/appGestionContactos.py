from EjSistemaGestionContactos.gestionContactos import GestionContactos


class AppGestionContactos:
    def __init__(self):
        self.gestion_contactos = GestionContactos()


    def menu(self):

        while True:
            print("\n*** App Gestión de Contactos ***")
            print("1. Agregar contacto")
            print("2. Mostrar contactos")
            print("3. Buscar contacto por nombre")
            print("4. Eliminar contacto por nombre")
            print("5. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                nombre = input("Nombre: ").strip()
                telefono = input("Teléfono: ").strip()
                email = input("Email: ").strip()
                self.gestion_contactos.agregar_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.gestion_contactos.mostrar_contactos()
            elif opcion == "3":
                nombre = input("Nombre a buscar: ").strip()
                self.gestion_contactos.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre a eliminar: ").strip()
                self.gestion_contactos.eliminar_contacto(nombre)
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")



if __name__ == "__main__":
    app = AppGestionContactos()
    app.menu()