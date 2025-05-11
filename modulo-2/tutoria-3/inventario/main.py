from inventario import Inventario
from electronico import Electronico

def main():
    inventario = Inventario()

    inventario.agregar_producto(Electronico("Laptop", 1000, 2))
    inventario.agregar_producto(Electronico("PC", 1000, 2))
    #inventario.agregar_producto(Alimento("Pan", 3))
    #inventario.agregar_producto(Ropa("Camiseta", 20))

    inventario.mostrar_productos()

if __name__ == "__main__":
    main()