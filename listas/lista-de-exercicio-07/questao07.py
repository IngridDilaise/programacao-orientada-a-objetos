class Pessoa:
	def __init__(self,nome,idade,peso,altura):
		self.nome=nome
		self.idade=idade
		self.peso=peso
		self.altura=altura

	def envelhecer(self):
		self.idade+=1

	def engordar(self):
		self.peso+=1

	def emagrecer(self):
		self.peso-=1


	def crescer(self):
		if self.idade<=21:
			self.altura+=0.5

		else:
			print("sua altura é: ",self.altura)

	def imprimir(self):
			print(f"nome:{self.nome}, idade:{self.idade}, peso:{self.peso},altura:{self.altura}")

pessoa1=Pessoa("Ingrid",20,56,1.57)
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()
pessoa1.imprimir()