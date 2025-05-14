from abc import ABC, abstractmethod
from typing import List
from almacenes.producto import Producto

    
#
#  Observer: distribuidor
#


class Distribuidor(ABC):
    def __init__(self, nombre:str, categorias_interes: List[str]):
        self.nombre = nombre
        self.categorias_interes = categorias_interes


    @abstractmethod
    def notificar(self, producto:Producto):
        pass