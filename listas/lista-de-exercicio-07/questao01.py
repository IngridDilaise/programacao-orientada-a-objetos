class Bola:

	def __init__(self,cor,circunferencia,material):
		self.cor=cor
		self.circunferencia=circunferencia
		self.material=material

	def trocar_cor(self,nova_cor):
		self.cor=nova_cor

	def mostrar_cor(self):
		print(self.cor)


bola1=Bola("verde",4,"couro")


bola1.mostrar_cor
bola1.trocar_cor("rosa")
print(bola1)
bola1.mostrar_cor()