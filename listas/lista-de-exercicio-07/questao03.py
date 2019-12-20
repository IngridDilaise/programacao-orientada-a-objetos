class Quadrado:

	def __init__(self,tamanho_lado):
		self.tamanho_lado=tamanho_lado

	def mudar_valor_lado(self,novo_tamanho_lado):
		self.tamanho_lado=novo_tamanho_lado
		return


	def retornar_valor_lado(self):
		return self.tamanho_lado

	def calcular_area(self):
		area=self.tamanho_lado*self.tamanho_lado
		return area

quadrado1=Quadrado(4)

quadrado1.mudar_valor_lado(3)
lado= quadrado1.retornar_valor_lado()
print("o novo valor do lado é: ",lado)

	
quadrado1.calcular_area()
print("a area é: ",quadrado1.calcular_area())




