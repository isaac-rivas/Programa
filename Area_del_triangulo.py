'''
Escribe un programa que solicite al usuario la Base y Altura de un triángulo y calcule su área.
 Recuerda la fórmula es Área = Base * Altura / 2 
Entrada: 
Dame Base 
>5 
Dame Altura >4 
Salida: 
El Área del triángulo es: 10 
'''
print ("Dame la base ")
base = int(input())
print("Dame la altura ")
altura = int(input())
area = base * altura / 2
print ("El Area del triangulo es: " + str(area))