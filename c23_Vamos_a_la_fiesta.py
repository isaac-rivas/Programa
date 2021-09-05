#Descripción: hoy es la fiesta de graduación y te dejaran ir en base a tus calificaciones del mes,
#  basadas en la siguiente condición: “podrás ir a la fiesta si pasaste la clase de matemáticas
#  y si en la de química obtuviste un 100”. Tu papa es muy corto de palabras y si no cumples con
#  las condiciones solo te dirá “gracias”, pero si cumples te dirá “SI vas a la fiesta, gracias”. 
# Consideración: Se entiende como calificación aprobatoria tener 60 o más. 

calif_mat = int(input('Calificacion de matematicas: '))
calif_qui = int(input('Calificacion de quimica: '))

calif_mes = (calif_qui + calif_mat) / 2

if calif_mes >= 70:
    print ('Si puedes ir a la fiesta, Gracias')
    calif_qui == 100
else:
    print ('Gracias!')