a=int(input("Digite o 1º numero:\n"))
b=int(input("Digite o 2º numero:\n"))
c=int(input("Digite o 3º numero:\n"))

menor=a

if b<a and b<c:
	menor=b
if c<a and c<b:
	menor=c 

maior=a
if b>a and b>c:
	maior=b
if c>a and c>b:
	maior=c

print("O MENOR NUMERO DIGITADO FOI {}".format(menor))
print("O MAIOR NUMERO DIGITADO FOI {}".format(maior))
