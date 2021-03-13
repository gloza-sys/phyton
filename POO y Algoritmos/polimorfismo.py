class Persona:
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def avanza(self):
        print("ando caminando")
    
class Ciclista(Persona):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)

    def avanza(self):
        print("Ando moviendome en mi bicicleta")
        #return super().avanza()

def main():
    persona = Persona("David")
    persona.avanza()

    ciclista = Ciclista("Daniel")
    ciclista.avanza()

if __name__ == "__main__":
    main()