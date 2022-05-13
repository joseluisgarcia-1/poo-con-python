class Rectangulo:
    def __init__(self, base, altura) -> None:
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == '__main__':
    #si queremos le pasamos así también los valores base=2, altura=4
    #rectangulo = Rectangulo(base=2,altura=4)
    rectangulo = Rectangulo(2,4)
    print(rectangulo.area())
    #si queremos le pasamos así también el valor, lado=5
    cuadrado = Cuadrado(5)
    #cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())