horario = input("Digite [M:Matutino, V=Vesperino, N:Noturno]: ")

if horario == 'M' or horario == 'm':
    print("Bom Dia")
elif horario == 'V' or horario == 'v':
    print("Boa Tarde")
elif horario == 'N' or horario == 'n':
    print("Boa Noite")
else:
    print("Valor Inválido")