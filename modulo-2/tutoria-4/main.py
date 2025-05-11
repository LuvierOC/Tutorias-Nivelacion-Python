from abc import ABC, abstractmethod
from typing import List

#
#  Producto y fabrica de Productos
#

class Producto:
    def __init__(self, nombre:str, categoria:str):
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria})"

    
class FrabricaProducto:
    @staticmethod
    def crear_producto(nombre:str, categoria:str)->  Producto:
        return Producto(nombre, categoria)



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

class DistribuidorConcreto(Distribuidor):
    def notificar(self, producto: Producto):
        print(f"[{self.nombre}] Notificado de nuevo Producto: {producto}")

    

#
#  Singleton: Estrategia de notificacion
#


class EstrategiaNotificacion(ABC):


    @abstractmethod

    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        pass


class NotificarATodos (EstrategiaNotificacion):
    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        print("-- Estrategia-- Notificar a todos los distribuidores")
        for d in distribuidores:
            d.notificar(producto)

class NotificarPorCategoria (EstrategiaNotificacion):
    def notificar(self, producto:Producto, distribuidores:List[Distribuidor]):
        print("-- Estrategia-- Notificar a los distribuidores que les conviene")
        for d in distribuidores:
           if producto.categoria in d.categorias_interes:
                d.notificar(producto)


#
#  Almacen (singleton + observer - sujeto + Stratategy )
#

class Almacen():

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

#
# Ejemplo
#

if __name__ == "__main__":

    d1 = DistribuidorConcreto("Distribuidora General", ["Tecnologia", "Ropa", "Alimentos"])

    d2 = DistribuidorConcreto("Distribuidora Fruver", ["Alimentos"])

    d3 = DistribuidorConcreto("Distribuidora Artesanias", ["Ropa"])


    estrategia_inicial = NotificarATodos()


    almacen = Almacen(estrategia_inicial)

    almacen.agregar_distribuidor(d1)
    almacen.agregar_distribuidor(d2)
    almacen.agregar_distribuidor(d3)

    p1 = FrabricaProducto.crear_producto("Blusa", "Ropa")

    almacen.agregar_producto(p1)