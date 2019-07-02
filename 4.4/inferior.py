from vip import *
#importando a classe pai

class Inferior(Vip):
    def __init__(self):
        super().__init__()
        self._tipo = "VIP"
        self._area = "Inferior"

    def Adicional(self):
        return 30

    def Imprimir(self):
        print("\nTIPO: {}\nAREA: {} | VALOR: {}".format(self._tipo, self._area, self.Price()))