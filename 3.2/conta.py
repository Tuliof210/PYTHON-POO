# coding: utf-8

#notação de arredondamento => "%.nf"%valor    =>n = casas decimais
class Conta:

    def __init__(self, e1, e2, e3, e4, e5, e6):
        self._titular = e1
        self._tipo = e2 #true corrente - false poupança
        self._saldo = e3
        self._numero = e4
        self._agencia = e5
        self._senha = e6
        self._historico = []


    def _Verificar(self, senha):
        if senha == self._senha:
            return True
        else:
            print("\nSenha Incorreta")
            return False

    @property
    def titular(self):
        #if self._Verificar(input("\nDigite sua senha: ")):
            return self._titular
    @property
    def tipo(self):
        #if self._Verificar(input("\nDigite sua senha: ")):
            return "corrente" if self._tipo else "poupança" #ternario
    @property
    def saldo(self):
        if self._Verificar(input("Digite sua senha: ")):
            return "\n--------------------------\nSeu saldo atual é de: R$ {}".format("%.2f"%self._saldo) #arredondamento
    @property
    def numero(self):
        #if self._Verificar(input("\nDigite sua senha: ")):
            return self._numero
    @property
    def agencia(self):
        #if self._Verificar(input("\nDigite sua senha: ")):
            return self._agencia


    def Depositar(self, d):
        if self._Verificar(input("Digite sua senha: ")):
            try:
                if float(d) < 1:
                    print("\nNão é possivel realizar depositos com valor inferior a R$ 1,00")
                else:
                    self._saldo+=float(d) #valor+=5 || valor = valor + 5 
                    self._historico+=[float(d)]
                    print("\nDeposito de R$ {} realizado com sucesso".format("%.2f"%float(d)))

            except:
                print("\nNão será aceito valores não-numericos")

    def Sacar(self, s):
        if self._Verificar(input("Digite sua senha: ")):
            try:
                if float(s) > self._saldo:
                    print("\nSaldo não disponivel")
                elif float(s) <= 0:
                    print("\nNão é possível sacar Valores negativos ou nulos")
                else:
                    self._saldo -= float(s)
                    self._historico+=[float(s) * -1]
                    print("\nSaque de R$ {} realizado com sucesso".format("%.2f"%float(s)))
            except:
                print("\nNão será aceito valores não-numericos")

    def Historico(self):
        if self._Verificar(input("Digite sua senha: ")):
            print("\n========================")
            if len(self._historico) == 0:
                print("\nALERTA: Essa conta não possui transações!")
            else:
                for i in self._historico:
                    if i < 0:
                        print(" - R$ {}".format("%.2f"%abs(i))) #abs retorna o valor absoluto de um numero
                    else:
                        print(" + R$ {}".format("%.2f"%abs(i)))
                print("========================\nSALDO ATUAL: R$ {}".format("%.2f"%self._saldo))



                
