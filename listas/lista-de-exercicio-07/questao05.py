class Pokemon:
	def __init__(self,nome,tipo,descricao,ataques,nivel,poder_luta,e_brilhante=True):

		self.nome=nome
		self.tipo=tipo
		self.descricao=descricao
		self.ataques=ataques
		self.nivel=nivel
		self.poder_luta=poder_luta
		self.e_brilhante=e_brilhante

	def mostrar_ataques(self):
		print(self.ataques)

	def subir_nivel(self):
		self.nivel+=1
		self.poder_luta+=1

	def mostrar_poder_luta(self):
		print(self.poder_luta)

	def e_brilhante(self):
		if e_brilhante==True:
			print("Brilhante")

		else:
			print("Nao Brilhante")

	def adicionar_ataque(self,novo_ataque):
		self.ataques.append(novo_ataque)

	def imprimir(self):
		print(f"nome:{self.nome}, tipo: {self.tipo}, descricao: {self.descricao}, ataques:{self.ataques}, nivel:{self.nivel}, poder_luta:{self.poder_luta}, e_brilhante:{self.e_brilhante}")
		


pokemon1=Pokemon("pikachu","raio","amarelo, pequeno",[],0,2)

pokemon1.adicionar_ataque("ataque_raio")
pokemon1.imprimir()
