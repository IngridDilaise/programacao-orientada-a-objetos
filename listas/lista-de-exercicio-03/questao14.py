nota1 = float(input("Digite a nota1"))
nota2 = float(input("Digite a nota2"))
media = (nota1 + nota2) / 2

if media >= 0 and media <= 4:
    print("conceito E")
elif media > 4 and media <= 6:
    print("conceito D")
elif media > 6 and media <= 7.5:
    print("conceito C")
elif media > 7.5 and media <= 9:
    print("conceito B")
else:
    print("conceito A")
