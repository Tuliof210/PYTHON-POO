import abc #importação da superclasse abstrata
#necessario para classes abstratas
#se uma classe abstrata herdar atributos de outra classe abstrada nao eh necessario importar o abc.ABC

class Ingresso(abc.ABC):
    def __init__(self):
        self._price = 50

    @abc.abstractmethod
    def Price(self):
        pass

    @abc.abstractmethod
    def Imprimir(self):
        pass
