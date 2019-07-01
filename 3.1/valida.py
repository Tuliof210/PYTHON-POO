

class Data:

    List_Dias_Mes = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    Dict_nomes = {1:"Janeiro", 2:"Fevereiro", 3:"Março", 4:"Abril", 5:"Maio", 6:"Junho", 7:"Julho", 8:"Agosto", 9:"Setembro", 10:"Outubro", 11:"Novembro", 12:"Dezembro"}

    def __init__(self):
        self._dia = 0
        self._mes = 0
        self._ano = 0
        self._bissexto = True #inicializar booleanos com true
        self._valida = True #aparentemente com false nao da para alterar
        self._existe = True

    @property
    def dia(self):
        return self._dia
    
    @property
    def mes(self):
        return self._mes 
    
    @property
    def ano(self):
        return self._ano

    @property
    def bissexto(self):
        return self._bissexto

    @property
    def valida(self):
        return self._valida

    @property
    def existe(self):
        return self._existe

    @dia.setter
    def dia(self, d):
        try:
            if d < 1 or d > 31:
                raise
            self._dia = d

        except:
            self._existe = False
            print("Valor de Dia invalido")

    @mes.setter
    def mes(self, m):
        try:
            if m < 1 or m > 12:
                raise
            self._mes = m

        except:
            self._existe = False
            print("Valor de mes invalido")

    @ano.setter
    def ano(self, a):
        try:
            if a < 1:
                raise 
            self._ano = a
            self._inexistente = False

        except:
            self._existe = False
            print("Valor de ano invalido")

    def Verificar(self):
        if self.ano % 4 != 0:
            self._bissexto = False
        elif self.ano % 100 != 0:
            self._bissexto = True
        elif self.ano % 400 != 0:
            self._bissexto = False
        else:
            self._bissexto = True

        if self.dia > Data.List_Dias_Mes[self.mes]:
            if self.dia == 29 and self._bissexto == True:
                self._valida = True
            else:
                self._valida = False

    def Nome_mes(self):
        return Data.Dict_nomes[self.mes]
