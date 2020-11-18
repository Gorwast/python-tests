

class Area:

    def __init__(self,base=0,altura=0):
        self.base = base
        self.altura = altura
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
