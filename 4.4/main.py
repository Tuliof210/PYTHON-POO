from normal import *
from ingresso import *
from vip import *
from superior import *
from inferior import *
from cliente import *
#usar nome dos arquivos e nao das classes

"""
a1 = Normal()
a2 = Superior()
a3 = Inferior()
print(a1.Imprimir())
print(a2.Imprimir())
print(a3.Imprimir())
"""
print("\nxxxxxxxxxxxxxxxxxxx\nCOMPRA DE INGRESSOS\nxxxxxxxxxxxxxxxxxxx")

def Intro():
	print("\n Ingresso Normal: R$ 50,00")
	print(" Ingresso Vip - Inferior: R$ 80,00")
	print(" Ingresso Vip - Superior: R$ 100,00")
	print("\n 1 - Normal || 2 - Vip Inferior || 3 - Vip Superior")

Intro()
input("\n Pressione qualquer tecla para começar a comprar...\n___________________________________________________")

i1 = Normal()
i2 = Inferior()
i3 = Superior()

pessoa = Cliente()

op = 0
quant = 0
#stay = True
confirma = ""

while True:
	try:
		op = int(input("\nQual ingresso deseja comprar? "))

		if op == 1:
			print("\nINGRESSO NORMAL\n++++++++++++++++++++++")
			quant = int(input("Quantos deseja Comprar? "))

			if quant == 0:
				raise

			i1.Imprimir()
			print("TOTAL: R$ {}".format("%.2f"%(i1.Price()*quant)))
			confirma = input("#####################################################\nConfirmar?(y/n): ")

			if confirma == "n":
				print("Compra Cancelada!")
				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue

			if confirma == "y":
				print("Compra Confirmada!")
				pessoa.Normal = quant

				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue

		if op == 2:
			print("\nINGRESSO VIP - Inferior\n++++++++++++++++++++++")
			quant = int(input("Quantos deseja Comprar? "))

			if quant == 0:
				raise

			i2.Imprimir()
			print("TOTAL: R$ {}".format("%.2f"%(i2.Price()*quant)))
			confirma = input("#####################################################\nConfirmar?(y/n): ")

			if confirma == "n":
				print("Compra Cancelada!")
				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue

			if confirma == "y":
				print("Compra Confirmada!")
				pessoa.Inferior = quant

				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue

		if op == 3:
			print("\nINGRESSO VIP - Superior\n++++++++++++++++++++++")
			quant = int(input("Quantos deseja Comprar? "))

			if quant == 0:
				raise

			i3.Imprimir()
			print("TOTAL: R$ {}".format("%.2f"%(i3.Price()*quant)))
			confirma = input("#####################################################\nConfirmar?(y/n): ")

			if confirma == "n":
				print("Compra Cancelada!")
				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue

			if confirma == "y":
				print("Compra Confirmada!")
				pessoa.Superior = quant

				confirma = input("\nDeseja continuar comprando?(y/n): ")

				if confirma == "n":
					print("\n\nPrograma encerrado...")
					break
				if confirma == "y":
					continue
	except:
		print("\nALERTA: ENTRADA DE PARAMETROS INVÁLIDOS")

print("\n\nSUA COMPRA:")
print("\nNORMAL: {}x R$ {} => R$ {}".format(pessoa.Normal, "%.2f"%i1.Price(), "%.2f"%(pessoa.Normal*i1.Price())))
print("VIP inferior: {}x R$ {} => R$ {}".format(pessoa.Inferior, "%.2f"%i2.Price(), "%.2f"%(pessoa.Inferior*i2.Price())))
print("VIP superior: {}x R$ {} => R$ {}".format(pessoa.Superior, "%.2f"%i2.Price(), "%.2f"%(pessoa.Superior*i3.Price())))
print("---------------------------------------------------------------------------------\nTOTAL: R$ {}".format("%.2f"%pessoa.Total()))