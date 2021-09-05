#Descripción: Realiza un programa que solicite al usuario el largo y ancho
#  y con estos valores nos dibuje un rectangulo

ancho = int(input('Ancho: '))
alto = int(input('Alto: '))

for i in range(alto):
    for j in range(ancho):
        print ('#', end='')
    print('')
