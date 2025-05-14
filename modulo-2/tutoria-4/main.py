from almacenes.almacen import Almacen
from distribuidores.distribuidor_concreto import DistribuidorConcreto
from estrategias.estrategia_notificar_po_categoria import NotificarPorCategoria
from estrategias.estrategia_notificar_a_todos import NotificarATodos
from almacenes.fabrica_producto import FrabricaProducto

def seleccionar_estrategia() -> object:
    print("Bienvenido al almacén")
    print("Estrategias vigentes:")
    print("1. Notificar a todos")
    print("2. Notificar por categorías")

    opcion = input("¿Qué estrategia eliges? (1 o 2): ").strip()

    match opcion:
        case "1":
            return NotificarATodos()
        case "2":
            return NotificarPorCategoria()
        case _:
            print("Opción no válida. Se usará 'Notificar a todos' por defecto.")
            return NotificarATodos()


def main() -> None:
    estrategia = seleccionar_estrategia()

    # Instancia singleton de Almacén
    almacen = Almacen(estrategia)

    # Distribuidores
    d1 = DistribuidorConcreto("Distribuidora General", ["Tecnologia", "Ropa", "Alimentos"])
    d2 = DistribuidorConcreto("Distribuidora Fruver", ["Alimentos"])
    d3 = DistribuidorConcreto("Distribuidora Artesanias", ["Ropa"])

    # Registro
    almacen.agregar_distribuidor(d1)
    almacen.agregar_distribuidor(d2)
    almacen.agregar_distribuidor(d3)

    # Productos
    producto = FrabricaProducto.crear_producto("Blusa", "Ropa")
    almacen.agregar_producto(producto)


if __name__ == "__main__":
    main()