class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saluda(self, otra_persona):
        return f'Hola {otra_persona.nombre} mi nombre es {self.nombre}'
        #la línea de abajo se usa con python3.6 en adelante
        #return f'Hola {otra_persona.nombre}, mi nombre es: {self.nombre}.'

messi = Persona('Lio', 34)
cr = Persona("Cr", 37)
#invocando la función saluda
messi.saluda("mbappe")
