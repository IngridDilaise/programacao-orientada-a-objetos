n1=int(input("Digite o 1º numero\n"))
n2=int(input("Digite o 2º numero\n"))
n3=int(input("Digite o 3º numero\n"))

if n1>n2 and n1>n3:
	print("O numero Maior é:\n",n1)
elif n2>n1 and n2>n3:
	print("O numero Maior é:\n",n2)
else:
	print("O numero Maior é:\n",n3)