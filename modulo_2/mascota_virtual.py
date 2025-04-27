class Mascota:

    def __init__(self, nombre = None, especie = None, edad=None):

        
        self.nombre = nombre
        self.edad = None
        self.velocidad = 30
        self.velocidad_maxima = None
        

        if nombre is not None and edad is not None and especie is not None:
            
            self.edad = edad + 5
            print("entro al segundo inicializador")
            print(f"Nombre de la mascota es: {self.nombre} y edad es {self.edad}")

        elif nombre is not None and edad is not None:
            self.edad = edad 
            print("entro al tercer inicializador")
            print(f"Nombre de la mascota es: {self.nombre} y edad es {self.edad}, tercer inicializador")


    def pedir_velocidad(self):
        velocidad_input = input("---- Digite la velocidad de la mascota---")

        self.velocidad = float(velocidad_input)
        self.velocidad_maxima = self.velocidad + 10

        print (f"La velocidad maxima de {self.nombre} es: {self.velocidad_maxima}")

    def velocidad_maxima_con_promedio(self, velocidad_promedio):
        self.velocidad = velocidad_promedio
        self.velocidad_maxima =self.velocidad + 10

    def __str__(self):
        return f"Mascota: {self.nombre}, Edad: {self.edad}, Velocidad maxima= {self.velocidad_maxima}"


