def elevar_numero(numero):
    return numero * numero * numero

print(elevar_numero(3))
print(elevar_numero(2))
print()
#declaro la variable nombre con el string "messi"
nombre = 'Messi'
#en esta función le paso el nombre
def presentarse(nombre):
	return f"Me llamo {nombre}"
#en esta función le paso el nombre pero ya lo saludo
def estudiemos_juntos(nombre):
	return f"¡Hey {nombre}, aprendamos Python!"
#en esta función le paso el nombre
def consume_funciones(funcion_entrante):
	#tambien se puede pasar así, se le pasa el string directo
    return funcion_entrante(nombre)
    #return presentarse("messi")
print(presentarse("ronaldo"))
print(estudiemos_juntos("ronaldo"))
print()
print(consume_funciones(presentarse))
print(consume_funciones(estudiemos_juntos))
print()
"""
en este tipo de funciones cuando se tiene una o más funciones dentro de otra función, las funciones que estén dentro de la función mayor no se ejecutan
hasta que la función mayor se ejecute, en este caso hasta que la funcion_mayor() no se ejecute las funciones frameworks y librerias() no se ejecutan
"""
def funcion_mayor():
	print("Esta es una función mayor y su mensaje de salida.")

	def librerias():
		print("Algunas librerías de Python son: Scikit-learn, NumPy y TensorFlow.")

	def frameworks():
		print("Algunos frameworks de Python son: Django, Dash y Flask.")

	frameworks()
	librerias()
funcion_mayor()