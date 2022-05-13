class Persona:

    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Estoy golpeando el balón")

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print("Estoy circulando en mi bicicleta")
    
def main():
    persona = Persona("Mbappe")
    persona.avanza()

    ciclista = Ciclista("Egan Bernal")
    ciclista.avanza()

if __name__ == '__main__':
    main()
        