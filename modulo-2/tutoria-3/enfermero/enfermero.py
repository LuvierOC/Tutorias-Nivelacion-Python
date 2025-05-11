class Enfermero:
    
    def __init__(self, nombre:str):
        self._nombre= nombre
        self.__turno = "noche"  # privado
        self.__sueldo = 4_000_000

    
    @property
    def sueldo(self):
        return self.__sueldo
    
    def _asignar_turno (self, turno):
        match(turno):
            case "mañana":
                return 2_000_000
            case "tarde":
                return 2_500_000
            case "noche":
                return 3_000_000
    
    @property
    def turno(self):
        return self.__turno
    
    @turno.setter
    def turno(self, nuevo_turno):
        if nuevo_turno in ["mañana", "tarde", "noche"]:
            self.__turno = nuevo_turno
            self.__sueldo = self._asignar_turno(nuevo_turno)

            

            #Al llamar atributos, recordar su moificador de acceso, debes fijarte en los "_"
            # "_nombre" protegido
            # "__turno" private


            print(f"Turno de {self._nombre} cambiado a {self.turno}.\nSaldo actualizado a  {self.sueldo:,}")

            #este self.turno se refiere al metodo getter (fijate que no posee ningun guion "_")
        else:
            raise ValueError("Valor incorrecto.")
    
