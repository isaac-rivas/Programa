import math

num = int(input('Digite un numero: '))

while num <0 :
    print ('Eroor -> deberia ser numero positivo')
    num = int(input('Digite un numero: '))

print (f'\nSu raiz cuadrada es: ({math.sqrt(num):.2f}')
