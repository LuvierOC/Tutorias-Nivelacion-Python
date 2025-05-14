from abc import ABC, abstractmethod
from typing import List
from almacenes.producto import Producto
from distribuidores.distribuidor import Distribuidor


class EstrategiaNotificacion(ABC):


    @abstractmethod

    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        pass