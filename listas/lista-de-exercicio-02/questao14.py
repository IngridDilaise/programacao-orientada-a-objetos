peso_peixes=float(input("Digite o peso total dos peixes:"))

if peso_peixes>50:
	excesso=peso_peixes-50
	multas=excesso*4
	print("O excesso de peso é:",excesso)
	print("O valor total das multas é:",multas)


else:

    print("peso dos peixes é:",peso_peixes)

 
