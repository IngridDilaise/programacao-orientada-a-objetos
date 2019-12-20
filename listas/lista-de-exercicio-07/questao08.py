class Tamagotchi:

	def __init__(self,nome):
		self.nome=nome
		self.fome=10
		self.saude=10
		self.idade=0

	def alterar_nome(self,novo_nome):
		self.nome=novo_nome

	def retornar_fome(self):
		return self.fome

	def retornar_saude(self):
		return self.saude

	def retornar_idade(self):
		return self.idade


	def comer(self):
		if self.fome==10:
			self.fome-=1
			print("sua fome apos comer é: ",self.fome)
		else:
			print(self.fome)

	def tomar_injecao(self):
		if self.saude<21:
			self.saude+=1
			print("Sua saude apos tomar injecao é: ",self.saude)
		else:
			print(self.saude)

	def envelhecer(self):
		if self.saude>0:
			self.saude-=1
			print("a sua saude apos envelhecer é: ",self.saude)
		else:
			print(self.saude)
		if self.idade==0:
			self.idade+=1
			print(self.saude)
		else:
			print(self.idade)

	def imprimir(self):
		print(f"nome:{self.nome},fome:{self.fome},saude:{self.saude},idade:{self.idade}")

tamagotchi1=Tamagotchi("isae")
tamagotchi1.imprimir()
tamagotchi1.comer()
tamagotchi1.tomar_injecao()
tamagotchi1.envelhecer()
