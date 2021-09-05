#Realiza un programa que imprima en pantalla la ecuación 10+4/2, 
# y mientras el usuario no la responda correctamente, la siga preguntado. 

while True:
    ecuacion = int(input("Dame la respuesta de la ecuación 10+4/2: "))
    if ecuacion == 12:
        break
    print (input('Dame la respuesta de la ecuacion 10+4/2: '))
print("Bien hecho, la respuestas es 12 ")