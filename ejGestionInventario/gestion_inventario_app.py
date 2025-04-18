from ejGestionInventario.producto import Producto
from ejGestionInventario.producto_dao import ProductoDAO

print("*** Gestión de Inventario ***")
opcion = None
while opcion != 6:
    print("""
    1. Mostrar productos
    2. Agregar producto
    3. Modificar producto
    4. Eliminar producto 
    5. Buscar producto
    6. Salir""")
    opcion = int(input("Introduce una opción(1-6): "))

    if opcion == 1:
        productos = ProductoDAO.seleccionar()
        print("\nLista de productos")
        for producto in productos:
            print(producto)
    elif opcion == 2:
        nombre_nuevo = input("Escribe el nombre: ")
        cantidad_nuevo = input("Escribe la cantidad: ")
        precio_nuevo = input("Escribe el precio: ")
        categoria_nuevo = input("Escribe la categoria: ")
        producto = Producto(nombre = nombre_nuevo, cantidad=cantidad_nuevo, precio=precio_nuevo, categoria=categoria_nuevo)
        productos_insertados = ProductoDAO.insertar(producto)
        print(f"Productos insertados: {productos_insertados}")
    elif opcion == 3:
        id_producto_nuevo = int(input("Escribe el id del producto a modificar: "))
        nombre_nuevo = input("Escribe el nombre: ")
        cantidad_nuevo = input("Escribe la cantidad: ")
        precio_nuevo = input("Escribe el precio: ")
        categoria_nuevo = input("Escribe la categoria: ")
        producto = Producto(id_producto_nuevo, nombre_nuevo, cantidad_nuevo, precio_nuevo, categoria_nuevo)
        productos_actualizados = ProductoDAO.actualizar(producto)
        print(f"Productos actualizados: {productos_actualizados}")
    elif opcion == 4:
        id_producto = int(input("Escribe el id del producto a eliminar: "))
        producto = Producto(id=id_producto)
        productos_eliminados = ProductoDAO.eliminar(producto)
        print(f"Productos eliminados: {productos_eliminados}")
    elif opcion == 5:
        nombre = input("Escribe el nombre del producto: ")
        print("\nProductos encontrados")
        productos = ProductoDAO.buscar(nombre)
        for producto in productos:
            print(producto)
    elif opcion == 6:
        print("Saliendo de la aplicación...")
    else:
        print("Opción inválida")
