import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierdo = lista[:medio]
        derecha = lista[medio:]
        print(izquierdo, '*'*5, derecha)
        #llamada recursiva en cada mitad
        
        ordenamiento_por_mezcla(izquierdo)
        ordenamiento_por_mezcla(derecha)
        
        #Iteradores para recorrer las dos listas
        i = 0
        j = 0
        
        #Iterador para la lista principal
        k = 0
        
        while i < len(izquierdo) and j < len(derecha):
            if izquierdo[i] < derecha[j]:
                lista[k] = izquierdo[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k+=1
        
        while i < len(izquierdo):
            lista[k] = izquierdo[i]
            i += 1
            k += 1
        
        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierdo}, derecha {derecha}')
        
    return lista

if __name__ == '__main__':
    tamano_de_lista = int(input("¿De qué tamaño será la lista?: "))
    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)
    print('-'*20)
    
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)