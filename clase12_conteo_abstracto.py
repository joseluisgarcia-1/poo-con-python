def f(x):
    respuesta = 0

    for i in range(x):
        print("iiiiiii",i)
        for j in range(x):
            print("jjjjjjjjjjj",j)
            respuesta += 1
            respuesta += 1
    return respuesta
"""
En este programa lo que le decimos es que por cada i desde 0 a 4, imprima en cada j los numeros del 0 al 4
"""
if __name__=='__main__':
    f(5)