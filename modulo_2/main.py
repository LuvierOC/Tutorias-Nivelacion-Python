from mascota_virtual import Mascota

def main():
    
    mascota3 = Mascota()

    mascota1 = Mascota("Spirit", "Perro", 12)

    mascota2 = Mascota("Leo", None, 12)
    
    print(mascota3)
    print(mascota1)
    print(mascota2)

    mascota2.velocidad_maxima_con_promedio(70)


    print(mascota2)


if __name__ == "__main__":
    main()