from modulo_2.tutoria_2.mascota_virtual import Mascota

def main():
    
    mascota1 = Mascota("Rex", "Dinosaurio") # va entrar en la primera instancia

    mascota2 = Mascota("Spirit", "Perro", 12) # va entrar en la segunda instancia

    mascota3 = Mascota("Leo", edad= 12) # va entrar en la tercera instancia.
    #tambien se puede expresar como  mascota3 = Mascota("Leo", None, 12)

    mascota4 = Mascota() # va entrar en la primera instancia

    print(mascota1)
    print(mascota2)
    print(mascota3)

    mascota3.obtener_velocidad_maxima(70)

    print(mascota3)

    mascota4.nombre = "Michi"
    mascota4.especie = "Gato"
    mascota4.edad = 5
    mascota4.pedir_velocidad_media()


    print(mascota4)


if __name__ == "__main__":
    main()