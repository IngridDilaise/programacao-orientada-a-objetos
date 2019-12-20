class Retangulo:

	def __init__(self,base,altura):

		self.base=base
		self.altura=altura

	def mudar_valor_lado(self,novo_valor):
		self.base=novo_valor

	def retornar_valor_lado(self):
		return self.novo_valor

	def calcular_area(self):
		area=self.base*self.altura
		return area
	def calcular_perimetro(self):
		perimetro=2*(self.base+self.altura)
		return perimetro

	def imprimir(self):
		print(f"area:{self.calcular_area()}, perimetro:{self.calcular_perimetro()}")

retangulo1=Retangulo(4,6)
retangulo1.imprimir()

