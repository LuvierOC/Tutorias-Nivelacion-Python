from .producto import Producto

class FrabricaProducto:
    @staticmethod
    def crear_producto(nombre: str, categoria: str) -> Producto:
        return Producto(nombre, categoria)