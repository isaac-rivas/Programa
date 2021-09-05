#•	A 30 o más grados centígrados vestirá “playera sin mangas y short” 
#•	si la temperatura marca menos de 30 pero más de 15 grados vestirá “playera y jeans” 
#•	si el termómetro marca temperatura negativa (< 0) usará su “gabardina y calentadores” 
# si la temperatura es cualquier otra, vestirá “suéter y pantalón” 

temperatura = int(input("Temperatura: "))

if temperatura >= 30:
    print("playera sin mangas y short. ")
elif temperatura > 15:
    print("playera y jeans. ")
elif temperatura < 0:
    print ("gabardina y calentadores. ")
else:
    print ("suéter y pantalón. ")