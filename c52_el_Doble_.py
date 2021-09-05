#Descripción: Realiza un programa que solicite al usuario un número,
# nos de cómo respuesta su doble y nos pregunte si deseamos continuar, }
# de ser la respuesta negativa el programa mostrará un mensaje de despedida y se terminará. 

while True:
    num = int(input("Dame un número: "))
    num1 = num * 2
    print("El doble del número", num, "es: ", num1)
    opc = input("¿Desea hacer otro calculo? S/N ")
    if opc.upper() == "S":
        print("Iniciando programa nuevamente")
    else:
        break
print("Gracias por usar el programa")