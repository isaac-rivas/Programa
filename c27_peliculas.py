#Descripción: El nuevo Cinema en tu ciudad está presentando 3 nuevas películas,
#  tú podrás asistir solo a UNA y será en base a tu edad. 
#Consideración: Las películas y sus edades permitidas son: 
#Sala A 	“Toy Story” 	Clasificación AA 	Edad 0 - 10 
#Sala B 	“Harry Potter y la Piedra Filosofal” 	Clasificación B 	Edad 11 - 15 
#Sala C 	“Eso” 	Clasificación C 	Edad 16 en adelante 

edad = int(input('Que edad tienes? '))

if edad <= 10:
    print ('Dirigirse a la Sala A, no olvides tus palomitas ')

elif edad <= 15:
    print ('Dirigirse a la Sala B, no olvides tus palomitas ')

elif edad >= 16:
    print ('Dirigirse a la Sala C, no olvides tus palomitas ')

