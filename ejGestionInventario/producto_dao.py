from ejGestionInventario.conexionDB import Conexion
from ejGestionInventario.producto import Producto


class ProductoDAO:
    SELECCIONAR = "SELECT * FROM productos ORDER BY id"
    INSERTAR = "INSERT INTO productos(nombre, cantidad, precio, categoria) VALUES(%s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE productos SET nombre=%s, cantidad = %s, precio=%s, categoria=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM productos WHERE id=%s"
    BUSCAR = "SELECT * FROM productos WHERE nombre=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f"Error al seleccionar productos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Error al insertar producto: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria, producto.id)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount

        except Exception as e:
            print(f"Error al actualizar producto: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def buscar(cls, nombre):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (nombre,)
            cursor.execute(cls.BUSCAR, valores)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto)
            return productos
        except Exception as e:
            print(f"Error al buscar producto: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
