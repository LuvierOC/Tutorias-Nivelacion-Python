from .distribuidor import Distribuidor
from almacenes.producto import Producto

class DistribuidorConcreto(Distribuidor):
    def notificar(self, producto: Producto):
        print(f"[{self.nombre}] Notificado de nuevo Producto: {producto}")