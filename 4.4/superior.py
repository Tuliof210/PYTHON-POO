from vip import *
#importando a classe pai

class Superior(Vip):
    def __init__(self):
        super().__init__()
        self._tipo = "VIP"
        self._area = "Superior"

    def Adicional(self):
        return 50

    def Imprimir(self):
        print("\nTIPO: {}\nAREA: {}\nVALOR: {}".format(self._tipo, self._area, self.Price()))
