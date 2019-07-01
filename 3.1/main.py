
from valida import * #importa toda a classe data

Datas = [] #lista de datas
Quant = 0 #quantidade de datas

try:
    Quant = int(input("Quantas datas? "))
except:
    print("\nVALOR INVALIDO")

for i in range(Quant): #preenche a lista
    aux = Data()
    Datas.append(aux)

try:
    for d in Datas: #Preenche os valores
        print("\n------------------------------------")
        d.dia = int(input("Digite uma valor para o dia: "))
        d.mes = int(input("Digite uma valor para o mes: "))
        d.ano = int(input("Digite uma valor para o ano: "))
        d.Verificar()
except:
    print("Foi informado algum valor invalido")

for x in Datas: #Printa os valores
    if x.existe:
        print("\n-------------------------------------------")
        print("Data: {}/{}/{}".format(x.dia, x.mes, x.ano))
        print("{} de {} de {}".format(x.dia, x.Nome_mes(), x.ano))
        print("Data Válida") if x.valida == True else print("Data Inválida") #Ternario
    
        if x.valida:
            print("Ano bissexto") if x.bissexto == True else print("Não é bissexto")
    