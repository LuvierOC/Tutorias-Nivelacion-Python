from .estrategia_notificacion_interface import EstrategiaNotificacion
from almacenes.producto import Producto
from distribuidores.distribuidor import Distribuidor
from typing import List

class NotificarPorCategoria (EstrategiaNotificacion):
    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        print("-- Estrategia-- Notificar a los distribuidores que les conviene")
        for d in distribuidores:
           if producto.categoria in d.categorias_interes:
                d.notificar(producto)