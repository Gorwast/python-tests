

class Area:

    def __init__(self):
        self.base = 0
        self.altura = 0
        print("Instancia a clase Area")

    def rectangulo(self, base, altura):

        self.base = base
        self.altura = altura
        return base * altura

    def triangulo(self, base, altura):
        self.base = base
        self.altura = altura
        return(base * altura)/2


obj1 = Area()
print(obj1.rectangulo(2, 2))
