class Caneta:

	def __init__(self,cor,marca,numero_ponta,volume_tinta):

		self.cor=cor
		self.marca=marca
		self.numero_ponta=numero_ponta
		self.volume_tinta=volume_tinta

	def encher_caneta(self):
		self.volume_tinta=50


    
	def escrever(self,palavra):
		print(palavra)
		self.volume_tinta-=1
	def retornar_marca(self):
		return self.marca

	def imprimir_caracteristicas(self):
		print(f"cor: {self.cor}, marca:{self.marca}, numero_ponta:{self.numero_ponta}, volume_tinta:{self.volume_tinta}")

caneta1=Caneta("preta","bic",4,50)
caneta1.encher_caneta()
caneta1.escrever("uma casa pequena")

caneta1.imprimir_caracteristicas()