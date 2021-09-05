def pideNumero(n):
    while True:
        num = input(f'Numero {n}: ')
        if num.isdigit():
            return int(num)
        print('el valor debe ser numerico. ')
    
num1 = pideNumero(1)
num2 = pideNumero(2)

mult = (num1) * (num2)
print (f'resultado: {mult}')