from enfermero import Enfermero


def main_enferemero():

    enfermero1= Enfermero(123)

    print(enfermero1.turno)
    input_turno = input("indroduzca el turno del enfermero: ")
    enfermero1.turno = input_turno


if __name__ == "__main__":
    main_enferemero()