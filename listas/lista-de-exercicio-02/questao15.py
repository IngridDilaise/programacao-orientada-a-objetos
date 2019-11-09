valor_hora=float(input("Quanto voce ganha por hora?\n"))
num_horas_mes=float(input("Quantas horas voce trabalha no mes?\n"))
salario_bruto=num_horas_mes*valor_hora
print("O seu salario bruto é:\n",salario_bruto)

impost_renda=salario_bruto*0.11
print("desconto do imposto de renda:\n",impost_renda)
desc_inss=salario_bruto*0.08
print("desconto do INSS",desc_inss)
sindicato=salario_bruto*0.05
print("desconto sindicato",sindicato)

descontos=impost_renda+desc_inss+sindicato

salario_liquido=salario_bruto-descontos
print("O seu salario liquido é:",salario_liquido)