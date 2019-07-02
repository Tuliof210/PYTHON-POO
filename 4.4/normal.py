from ingresso import *
#Importar a classe pai

class Normal(Ingresso):
    def __init__(self):
        super().__init__() #utiliza tudo que há no construtor pai
        #abaixo dele podemos adicionar mais atributos para a construção
        self._tipo = "Normal"

    def Price(self):
        return self._price

    def Imprimir(self):
        print("\nTIPO: {} | VALOR: R$ {}".format(self._tipo, self.Price()))
