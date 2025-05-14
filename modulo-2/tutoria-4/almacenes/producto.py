#
#  Producto y fabrica de Productos
#

class Producto:
    def __init__(self, nombre:str, categoria:str) -> None:
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria})"

    
