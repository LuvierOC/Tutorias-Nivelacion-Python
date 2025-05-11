# Vamos a generar un meno para gestionar la asistencia a una empresa de manera presencial


asistentes = []

MAX_ASISTENTES = 5


def mostrar_menu():
    print("\n--- Registro de asistencia ---")
    print("1. Registrar asistencia")
    print("2. Ver lista de asistentes")
    print("3. Ver cantidad de asistentes")
    print("4. Salir")


def registrar_asistentecia():
    if len(asistentes) < MAX_ASISTENTES:
        nombre = input("ingrese su nombre:")
        asistentes.append(nombre)
        print(f"Asistencia registrada para: {nombre}")
    else:
        print("La asistencia esta llena.")

def ver_lista_asistencia():
    if asistentes:
        print("Estudiantes presentess:")
        for i, nombre in enumerate(asistentes, start=1):
            print((f"{i}. {nombre}"))
    else:
        print("No existen asistencias...")


def contar_asistencia():
    print(f" Cantidad total de asistentes: {len(asistentes)}")


def ejecutar_sistema():
    while True:
        mostrar_menu()
        opcion = input("Seleccionar una opcion:")
        if opcion == "1":
            registrar_asistentecia()
        elif opcion == "2":
            ver_lista_asistencia()
        elif opcion == "3":
            contar_asistencia()
        elif opcion == "4":
            print("Salliendo de la aplicacion...\n")
            break
        else:
            print("Opcion no valida, vuelva a digitar")

ejecutar_sistema()
