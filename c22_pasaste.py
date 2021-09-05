#Se requiere un programa que permita la entrada al circo a todos aquellos estudiantes que hayan pasado el semestre, 
# para ello recibiremos su calificación de español y Matemáticas. 
#Consideración: la calificación aprobatoria es cuando el promedio de las 2 materias es igual o
#  mayor a 60. 
# La calificación deberá capturarse en números enteros en un rango de 0 a 100 

calif_mat = int(input("Calificacion de matematicas "))
calif_esp = int(input("Calificacion de español "))

promedio = (calif_mat + calif_esp) / 2

if promedio >= 60:
    print ("Bienvenido al circo \nGracias por venir. ")