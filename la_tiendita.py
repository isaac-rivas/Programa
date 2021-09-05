'''Escribe un programa que simule las compras de un cliente en nuestra tienda de abarrotes.
 El cliente comprará 3 productos distintos, cada uno en X cantidad. 
 La tienda deberá dar; el subtotal, el IVA correspondiente, y el total final. 
 Por ser día de la Independencia habrá un descuento del 20% sobre el total.
 Se le preguntará al usuario con cuanto pagará y se le informará cuál es su cambio.
 Salida:
El Subtotal de tu compra es: 100 
El IVA es: 15 
El Total: 115 
Descuento: 23 
El Total Final es: 92 
¿Con cuanto pagas? 
>100 
Tu cambio es: 8 
¡Gracias por tu Compra'''

producto1 = int(input("Producto 1 "))
producto2 = int(input("Prodcuto 2 "))
producto3 = int(input("Producto3  "))
subtotal = producto1 + producto2 + producto3
print (f"El subtotal de tu compra es:  {subtotal}")
iva = subtotal * .16
print (f"El IVA es: {iva}")
total = subtotal + iva
print (f"Total: {total}")
descuento = total * .20
print(f"Descuento: {descuento}")
totalfinal = total - descuento
print (f"Total final es: {totalfinal}")

pago = int(input("¿Con cuanto pagas?"))
cambio = pago - totalfinal
print(f"Tu cambio es: {cambio}")

print("!GRACIAS POR TU COMPRA")
