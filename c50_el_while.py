#Descripción: Desarrolla un programa que solicite al usuario un número y se repita 
# mientras este número sea par, y nos indique al final cuantos números 
# pares consecutivos le dio el usuario 

contador = 0
''''
num = 0

while num % 2 == 0:
    contador += 1
    num = int(input('Dame un numero par: '))

print(f'Escribiste {contador} numeors pares consecutivos. ')
'''

while True:
    num = int(input('Dame un numero par: '))
    if num % 2 == 0:
        contador += 1
    else:
        break

print (f'Escribiste {contador} numeros pares consecutivos. ')
