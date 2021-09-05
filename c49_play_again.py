#Descripción: Desarrolla un programa que solicite al usuario 2 calificaciones y 
# le dé su promedio y se repita hasta que el usuario le indique al 
# sistema que ya no desea seguir haciendo cálculos. 
#lower = convierte el valor en minuscula 

repetir = 's'

while repetir.lower() == 's':
    cal1 = int (input('Calificacion 1: '))
    cal2 = int(input('Calificacion 2: '))
    print('Tu calificacion es', (cal1 + cal2) / 2)
    repetir = input ('¿Deseas otro calculo (s/n: ')

print('¡Gracias por usar el sistema!')
