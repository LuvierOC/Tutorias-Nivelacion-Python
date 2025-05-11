from abc import ABC , abstractmethod

class Producto(ABC):
    
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_precio_final():
        pass

    def __str__(self):
        return f"{self.nombre} - Precio final: ${self.calcular_precio_final():.2f}"
    
    
