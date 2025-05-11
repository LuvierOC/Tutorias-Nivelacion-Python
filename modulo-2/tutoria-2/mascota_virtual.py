class Mascota:

    def __init__(self, nombre = None, especie = None, edad = None):
                
        self.nombre = nombre
        self.edad = edad
        self.especie = especie
        self.velocidad_media = None
        self.velocidad_maxima = None

        print("entro al primer inicializador")

        if nombre is not None and edad is not None and especie is not None:
            
            self.edad = edad + 10
            print("entro al segundo inicializador")
            print(f"Nombre de la mascota es: {self.nombre} y edad es {self.edad} segundo inicializador")

        elif nombre is not None and edad is not None:
            self.edad = edad 
            print("entro al tercer inicializador")
            print(f"Nombre de la mascota es: {self.nombre} y edad es {self.edad}, tercer inicializador")


    def pedir_velocidad_media(self):
        print("\nUsando el metodo obtener_velocidad_media.\n")
        
        velocidad_input = input("---- Digite la velocidad media de la mascota---\n")

        self.velocidad_media = float(velocidad_input)
        self.velocidad_maxima = self.velocidad_media + 10

        print (f"La velocidad maxima de {self.nombre} es: {self.velocidad_maxima}")

    def obtener_velocidad_maxima(self, velocidad_media):
        print("\nUsando el metodo obtener_velocidad_maxima.\n")
        self.velocidad_media = velocidad_media
        self.velocidad_maxima =self.velocidad_media + 10


    def __str__(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Velocidad maxima= {self.velocidad_maxima}, Especie: {self.especie}"