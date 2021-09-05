#: Para entrar a la fiesta de graduación deberás ser mayor de edad,
#  para lo cual deberás desarrollar un programa que solicite al usuario su edad actual y 
# con ella nos diga si es aceptado en la fiesta o no lo es. 

edad = int(input("Cuantos años tines? "))

if edad >= 18: 
    print ("Puedes pasar a la fiesta, bienvenido. ")
else:
    print ("Lo sentimos, no puedes ingresar. ")