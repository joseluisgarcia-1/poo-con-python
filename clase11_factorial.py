import time
import sys 
#con este cambiamos el límite de recursividad tener claro que es el set
sys.setrecursionlimit(1000000)
#con este podemos ver o imprimir el límite de recursividad tener claro que es el get
print(sys.getrecursionlimit())

def factorial(n):
    respuesta = 1
    while n >1:
        respuesta *= n
        n-=1
    return respuesta

def factorial_r(n):
    if n == 1:
        return 1
    return n * factorial_r(n-1)

if __name__ == '__main__':
    n = 10000
    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(final - comienzo)