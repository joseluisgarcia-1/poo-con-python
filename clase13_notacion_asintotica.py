#decimos que esta función crece de manera lineal y se denota como que crece de manera O(n)
"""def f(n):
    for i in range(n):
        print(i)
"""

#ley de la suma
def f(n):
    for i in range(n):
        print(i)
    
    for i in range(n*n):
        print(i)
#O(n) + O(n*n) = O(n+n^2) = O(n^2)

#ley de la multiplicación
def f_m(n):
    for i in range(n):
        for j in range(n):
            print(i,j)
#O(n) * O(n) = O(n*n) = O(n^2)

#Recursividad múltiple
def fibonacci(n):
    #if n == 0 or n == 1:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
#O(2**n)

if __name__ == '__main__':
    f_m(5)
    print("****",fibonacci(7))