preco1 = float(input("Digite o primeiro preço: "))
preco2 = float(input("Digite o segundo preço: "))
preco3 = float(input("Digite o terceiro preço: "))

lista = [preco1, preco2, preco3]

print("O produto que deve ser comprado é o que custa ", min(lista))