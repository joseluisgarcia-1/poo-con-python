"""
Borrar nombres que tengan una letra específica
"""

futbolistas = ["Son" ,"Diaz", "Mitrovic","Mané", "Salah", "Davinson", "Mohaed", "Virgil", "Alisson", "Dario"]
#print(futbolistas)

for l in futbolistas:
    if "M" in l:
        futbolistas.remove(l)
        #print(futbolistas)
#print(futbolistas)
"""
En este ejercicio no se está borrando los datos adecuadamente por la siguiente razón: lo que pasa es que cuando el for
empieza a hacer su recorrido y aplica el metodo remove, lo que sucede es que la lista empieza a cambiar su dimensión y 
en el momento que se elimina un dato, obviamente el número de datos se altera, es decir, cambia los indices, entonces cuenta
al elemento que procede y por esa razón se salta un elemento, y así sucesivamente se va saltando los elementos
Entonces hay dos formas de hacer eso de otra manera y es así:
"""
print()
coches = ["Bmw", "Mercedes", "Ferrari", "Mazda", "Renault", "Toyota", "Talbot", "Telsa", "Tatra"]

copia_coches = list(coches)
for coche in copia_coches:
    if "T" in coche:
        coches.remove(coche)
print(coches)
"""
Lo que se hizo en las líneas anteriores fue crear una lista copia de los coches y decirle que si en la lista copia
hay un coche o elemento que tenga la letra T lo elimine de la lista original
"""
"""
Otra forma es así:
"""
objetos = ["Nave", "Moto", "Carro", "Avión", "Nevera", "Nido", "Balón", "Canillera"]

copia_objetos = list(objetos)

for objeto in range(len(objetos)-1,-1,-1):
    if "N" in objetos[objeto]:
        objetos.remove(objetos[objeto])
print(objetos)
"""
explicación del código anterior: el range(len(objetos)-1,-1,-1)
donde el range(len(objetos)), cuenta los elementos que hay en la lista de objetos
y los -1,-1,-1
el primer -1 cuenta de atrás pa delante desde el último elemento de la lista hasta el primero y ese lo hace con el segundo -1
y el tercer -1, lo que hace es indicarle al código que se devuelva de uno en uno pero de atrás para adelante
la iteración se va a hacer por indices, por eso se pone if "N" in objetos[objeto]:
"""
"""
Programa que elimina los datos repetidos de una lista, y quedan sólo los únicos
"""
numbers = [1,2,3,4,5,1,2,3,4,4,6,7,8,9,0,1,1,3,12]
unicos = []

copia_numeros = list(numbers)

for n in copia_numeros:
    if n not in unicos:
        unicos.append(n)
    else:
        #copia_numeros.remove(n)
        numbers.remove(n)
        
#print("lista inicial",numbers)
#print(unicos)