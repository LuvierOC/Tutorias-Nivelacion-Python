from estrategias.estrategia_notificacion_interface import EstrategiaNotificacion
from typing import List
from almacenes.producto import Producto
from distribuidores.distribuidor import Distribuidor


class Almacen:

    _instancia = None

    def __new__(cls, *args, **kgars):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def __init__(self, estrategia:EstrategiaNotificacion):
        if not hasattr(self, '_inicializado'):
            self.distribuidores:  List [Distribuidor] = []
            self.productos:  List [Producto] = []
            self.estrategia = estrategia
            self._inicializado = True

    def agregar_distribuidor(self, distribuidor:Distribuidor):
        self.distribuidores.append(distribuidor)
    
    def agregar_producto(self, producto:Producto):
        self.productos.append(producto)
        print(f'\n [Almacen] Producto agregado: {producto}')
        self.estrategia.notificar(producto, self.distribuidores)


    def establecer_estrategia(self, estrategia:EstrategiaNotificacion):
        self.estrategia = estrategia