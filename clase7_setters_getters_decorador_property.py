from cgi import print_form


def funcion_decoradora(funcion):
	def wrapper():
		print("Este es el último mensaje...")
		funcion()
		print("Este es el primer mensaje ;)")
	return wrapper

#como decorador le pasamos el @funcion_decoradora
@funcion_decoradora
def zumbido():
	print("Buzzzzzz")

zumbido()
#zumbido = funcion_decoradora(zumbido)
#print(zumbido)

class Millas:
    def __init__(self, distancia=0):
        self.distancia = distancia
    
    def convertir_a_km(self):
        return self.distancia * 1.609
    
#creamos un nuevo objeto, es decir instanciamos
vuelo = Millas()
#pasamos la distancia
vuelo.distancia = 200
#vuelo.distancia = 300
#obtenemos el valor del atributo distancia
#print(vuelo.distancia)
#recibimos el método convertir_a_km
print(vuelo.convertir_a_km())

"""
lo que pasa ahí es que primero se instancia en la variable vuelo la clase Millas que trae como parámetro a distancia en valor 0
y luego a distancia se le re asigna el valor a 200 que es el valor que se transforma
"""

#incluyendo el metodo getter y setter

class MillasNuevo:
    def __init__(self, _distancia=0):
        self._distancia = _distancia
    
    def convertir_a_km(self):
        return self._distancia * 1.609

    #metodo getter
    def obtener_distancia(self):
        return self._distancia
    
    #metodo setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No se pueden convertir distancias menores que 0")
        self._distancia = valor
#valor = -33
volar = MillasNuevo()
volar._distancia = 345
print(volar.obtener_distancia())
print(volar.definir_distancia(2))

print()
"""
nuevo caso
"""
class MillasNew():
    def __init__(self):
        self._distancia = 0

    #Función para obtener el valor de _distancia
    def obtener_distancia(self):
        print("Llamado al método getter")
        return self._distancia
    
    #Función para definir el valor de distancia
    def definir_distancia(self, recorrido):
        print("Llamado al méotodo setter")
        self._distancia = recorrido

    #Función para eliminar el atributo _distancia
    def eliminar_distancia(self):
        del self._distancia
    
    distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)

#creamos el objeto
plane = MillasNew()
#pasamos la distancia
plane.distancia = 77
#obtenemos el atributo distancia
print(plane.distancia)

class MillasThree():
    def __init__(self):
        self._distancia = 0
    
    #función para obtener el valor de _distancia
    #Usando el decorador @property

    @property
    def obtener_distancia(self):
        print("Llamando al método getter en la nueva clase")
        return self._distancia

    #Función para definir el valor de _distancia
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible comvertir valores inferiores a 0")
        print("Llamado al método setter")
        self._distancia = valor

plane_new = MillasThree()
plane_new._distancia = 333
print(plane_new.definir_distancia)