import random 

def busqueda_binaria(lista, inicio, fin, objetivo):
    print(f'buscando {objetivo} entre {lista[inicio]} y {lista[fin -1]}')
    #si pasa esto quiere decir que el programa termina
    if inicio > fin:
        return False
    #si lo anterior no es cierto, se divide la lista en dos, como indicamos en la siguiente línea
    medio = (inicio + fin) // 2
    #si la lista en el índice medio es igual que el objetivo, retorne True
    if lista[medio] == objetivo:
        return True
    #si no, si el índice del medio de la lista es menor que el objetivo, entonces ejecute la función busqueda_binaria junto con sus parámetros
    #como estamos en el lado menor es decir un valor menor que el objetivo, entonces empezamos de la mitad hacia adelante por eso el medio + 1
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, fin, objetivo)
    else:
        return busqueda_binaria(lista, inicio, medio -1, objetivo)

if __name__ == '__main__':
    tamano_de_lista = int(input("¿De qué tamaño es la lista?: "))
    objetivo = int(input("¿Qué número quieres encontrar?: "))
    
    lista = sorted([random.randint(0,100) for i in range(tamano_de_lista)])
    
    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)
    
    print(lista)
    print(f'El número {objetivo} {"está" if encontrado else "no está"} en la lista')    