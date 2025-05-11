from producto import Producto

class Electronico (Producto):

    def __init__(self, nombre, precio_base, garantia_años):
        super().__init__(nombre, precio_base)
        self.garantia_años = garantia_años

    def calcular_precio_final(self):
        impuesto = 0.15 * self.precio_base
        garantia_extra = 20 * self.garantia_años
        return self.precio_base + impuesto + garantia_extra