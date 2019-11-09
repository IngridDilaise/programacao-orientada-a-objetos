with open ("amazon.csv") as arquivo:
	q1=(0)
	q2=(0)
	q3=(0)
	q4=(0)
	q_extra1=(0)
	q_extra2=(0)
	q_extra3=(0)
	q_extra4=(0)
	for linha in arquivo:
		informacoes=linha.strip("\n").split(",")
		numero_queimadas=informacoes[3].replace(".","")

		if ((informacoes[1]=='"Acre"') and (int(informacoes[0])==2015)):
			q1+=int(numero_queimadas)
		elif((informacoes[1]=='"Ceara"') and (int(informacoes[0])==2014)):
			q2+=int(numero_queimadas)
		elif((informacoes[1]=='"Amazonas"')):
			q3+=int(numero_queimadas)
		
		if((informacoes[0]=='"year"')):
			continue
		elif((int(informacoes[0])>=2010) and (informacoes[1]=='"Mato Grosso"')):
			q4+=int(numero_queimadas)

		elif((informacoes[1])=='"Amapa"'):
			q_extra1+=int(numero_queimadas)
		
		elif((informacoes[1])=='"Alagoas"') and (int(informacoes[0])>=2000):
			q_extra2+=int(numero_queimadas)

		elif((informacoes[1])=='"Bahia"'):
			q_extra3+=int(numero_queimadas)
		elif((informacoes[1])=='"Distrito Federal"') and (int(informacoes[0])==2010):
			q_extra4+=int(numero_queimadas)

		


print("Em 2015 o Acre teve {} queimadas".format(q1))
print("Em 2014 o Ceará teve {} queimadas".format(q2))
print("Na Amazonas foram {} queimadas".format(q3))
print("No Mato Grosso foram {} queimadas".format(q4))
print("No Amapa foram {} queimadas".format(q_extra1))
print("Na Alagoas de 2000 pra frente foram {} queimadas".format(q_extra2))
print("Na Bahia foram {} queimadas".format(q_extra3))
print ("Em 2010 no Distrito Federal foram {} queimadas".format(q_extra4))
