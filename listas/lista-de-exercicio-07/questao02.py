class Computador:
	def __init__(self,marca,modelo,componentes,anos_uso,cor):
		self.marca=marca
		self.modelo=modelo
		self.componentes=componentes
		self.anos_uso=anos_uso
		self.cor=cor

	def mostrar_marca(self):
		print(mostrar_marca)

	def adicionar_componentes(self,novo_componente):
		self.adicionar_componentes=novo_componente

	def mostrar_componentes(self):
		print(self.componentes)

	def mostrar_anos_uso(self):
		if (self.anos_uso >=6):
			print("Seu computador esta tão velho que tem problema de junta...juna tudo e joga fora...")
		else:
			print(self.anos_uso)

	def envelhecer(self):
		self.anos_uso+=1

computador1=Computador("asus",4,["monitor","mause","teclado","cpu"],7,"vermelho")
computador1.adicionar_componentes("memoria")

computador1.mostrar_componentes()
computador1.mostrar_anos_uso()