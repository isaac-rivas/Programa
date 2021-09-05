class rectangulo:
    base_r = 0
    altura_r = 0

    def altura(self):
        return self.altura_r

    def area(self):
        return self.base_r * self.altura_r

    def prisma(self):
        return self.area() * self.altura_r

    def piramide(self):
        return self.prisma() / 3

a = rectangulo()
a.altura = float(input('altura: '))
a.area = float(input('area: '))
print ('volumen del prisma:', a.prisma())
print ('volumen de la piramide;',a.piramide())