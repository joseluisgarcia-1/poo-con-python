"""
los valores hace referencia a lo que puede o está en la capacidad de cargar el morral
n = elementos
"""
def morral(tamanio_morral, pesos, valores, n):
    #si no nos quedan más elementos o el tamaño del morral ya es cero, es decir, el morral está lleno, se retorna 0
    if n == 0:
        return 0
    
    #validación de si lo que yo quiero meter en el morral, pesa más que la capacidad del morral
    
    if pesos[n-1] > tamanio_morral:
        return morral(tamanio_morral, pesos, valores, n-1)
    
    return max(valores[n-1]+morral(tamanio_morral-pesos[n-1], pesos, valores, n-1),
               morral(tamanio_morral, pesos, valores, n-1))
    
if __name__ == '__main__':
    valores = [60, 100, 120]
    pesos = [10,20,30]
    #este valor determina cuánto peso puedo cargar por ejemplo con un morral de 50 puedo cargar 220
    tamanio_morral = 900
    n = len(valores)
    
    resultado = morral(tamanio_morral, pesos, valores, n)
    print(resultado)
    