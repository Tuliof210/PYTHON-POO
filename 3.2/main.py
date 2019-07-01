# coding: utf-8
from random import randint
from conta import *


#NECESSARIO REALIZAR CORREÇOES EM SAQUE


def Intro():
    print("------------------------------------------------\n")
    print(" Digite 1 para CRIAR CONTA CORRENTE")
    print(" Digite 2 para CRIAR CONTA POUPANÇA")
    print(" Digite 3 para SACAR DE UMA CONTA")
    print(" Digite 4 para DEPOSITAR EM UMA CONTA")
    print(" Digite 5 para VERIFICAR O SALDO DE UMA CONTA")
    print(" Digite 6 para VER A LISTA DE CONTAS")
    print(" Digite 7 para VER HISTORICO DE UMA CONTA")
    print(" Digite 8 para SAIR DO PROGRAMA")

    print("\n------------------------------------------------\n Digite 0 para REEXIBIR O MENU\n------------------------------------------------")

def Cria_conta_corrente(lista_c):
    x1 = input("Informe o titular: ")
    x2 = input("Senha: ")

    x3 = randint(10000,99999) #numero da conta
    x4 = randint(1,9) #agencia

    print("Conta: {} - Agencia: {}".format(x3,x4))
    aux = Conta(x1, True, 0.0, x3, x4, x2) #titular, tipo, saldo, num, agencia, senha
    print("\nConta criada com sucesso!")
    lista_c.append(aux)

def Cria_conta_poupa(lista_p):
    x1 = input("Informe o titular: ")
    x2 = input("Senha: ")

    x3 = randint(10000,99999) #numero da conta
    x4 = randint(1,9) #agencia

    print("Conta: {} - Agencia: {}".format(x3,x4))
    aux = Conta(x1, False, 0.0, x3, x4, x2) #titular, tipo, saldo, num, agencia, senha
    print("\nConta criada com sucesso!")
    lista_p.append(aux)

def Lista_Contas(lista_c, lista_p):

    print("\nLista de Contas Corrente\n---------------------------------------")
    for i in lista_c:
        print("Conta/Agencia: {}-{} Titular: {}".format(i.numero, i.agencia, i.titular))

    print("\nLista de Contas Poupança\n---------------------------------------")
    for j in lista_p:
        print("Conta/Agencia: {}-{} Titular: {}".format(j.numero, j.agencia, j.titular))

def Sacar_Conta(lista_c, lista_p):
    try:
        val1 = int(input("\nDigite o Numero da conta: "))
        invalida = True

        for a in lista_c:
            if a.numero == val1:
                a.Sacar(input("Digite quanto deseja Sacar: "))
                invalida = False
                break

        for b in lista_p:
            if b.numero == val1:
                b.Sacar(input("Digite quanto deseja Sacar: "))
                invalida = False
                break

        if invalida:
            print("Conta invalida")
    except:
        print("Parametros invalidos")

def Depositar_Conta(lista_c, lista_p):
    try:
        val1 = int(input("\nDigite o Numero da conta: "))
        invalida = True

        for a in lista_c:
            if a.numero == val1:
                a.Depositar(input("Digite quanto deseja Depositar: "))
                invalida = False
                break

        for b in lista_p:
            if b.numero == val1:
                b.Depositar(input("Digite quanto deseja Depositar: "))
                invalida = False
                break

        if invalida:
            print("Conta Invalida")
    except:
        print("Parametros invalidos")
        
def Saldo_Conta(lista_c, lista_p):
    try:
        val1 = int(input("\nDigite o Numero da conta: "))
        invalida = True

        for a in lista_c:
            if a.numero == val1:
                print(a.saldo)
                invalida = False
                break

        for b in lista_p:
            if b.numero == val1:
                print(b.saldo)
                invalida = False
                break

        if invalida:
            print("Conta Invalida")
    except:
        print("Parametros invalidos")

def Historico_Conta(lista_c, lista_p):
    try:
        val1 = int(input("\nDigite o Numero da conta: "))
        invalida = True

        for a in lista_c:
            if a.numero == val1:
                a.Historico()
                invalida = False
                break

        for b in lista_p:
            if b.numero == val1:
                b.Historico()
                invalida = False
                break

        if invalida:
            print("Conta Invalida")
    except:
        print("Parametros invalidos")


L_Co = []
L_Po = []
op = ""

print("\nPROGRAMA SIMULADOR DE BANCOS\n________________________________________________________")
input("\nPress any key to continue...\n")
Intro()

while op != "8":
    op = input("\nEscolha uma opçao: ")

    if op == "1":
        print("\nCRIAR CONTA CORRENTE\n================================")
        Cria_conta_corrente(L_Co)

    elif op == "2":
        print("\nCRIAR CONTA POUPANÇA\n================================")
        Cria_conta_poupa(L_Po)

    elif op == "3":
        print("\nSACAR DE UMA CONTA\n================================")
        if len(L_Co) == 0 and len(L_Po) == 0:
            print("Não há contas cadastradas!")
            continue
        Sacar_Conta(L_Co, L_Po) 

    elif op == "4":
        print("\nDEPOSITAR EM UMA CONTA\n================================")
        if len(L_Co) == 0 and len(L_Po) == 0:
            print("Não há contas cadastradas!")
            continue
        Depositar_Conta(L_Co, L_Po)

    elif op == "5":
        print("\nSALDO DE UMA CONTA\n================================")
        if len(L_Co) == 0 and len(L_Po) == 0:
            print("Não há contas cadastradas!")
            continue
        Saldo_Conta(L_Co, L_Po)

    elif op == "6":
        print("\nLISTA DE UMA CONTAS\n================================")
        Lista_Contas(L_Co, L_Po)

    elif op == "7":
        print("\nHISTORICO DE UMA CONTA\n================================")
        Historico_Conta(L_Co, L_Po)

    elif op == "8":
        print("\nPrograma Finalizado com sucesso!")
        input("Presse any key to continue....")

    elif op == "0":
        Intro()

    else:
        print("VALOR INVALIDO")
