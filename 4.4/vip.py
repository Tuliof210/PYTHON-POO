from ingresso import *
#importando a classe pai

class Vip(Ingresso):
    def Price(self):
        return self._price + self.Adicional()

    @abc.abstractmethod
    def Adicional(self):
        pass