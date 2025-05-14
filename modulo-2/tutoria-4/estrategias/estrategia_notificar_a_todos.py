from .estrategia_notificacion_interface import EstrategiaNotificacion
from almacenes.producto import Producto
from distribuidores.distribuidor import Distribuidor
from typing import List

class NotificarATodos(EstrategiaNotificacion):
    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        print("-- Estrategia-- Notificar a todos los distribuidores")
        for d in distribuidores:
            d.notificar(producto)