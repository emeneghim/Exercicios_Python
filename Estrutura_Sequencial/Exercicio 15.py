horas_trabalhadas = int(input("Insira quantas horas voce trabalha por mes: "))
hora_ganha = float(input("Insira quanto voce ganha por hora: "))
salario_liquido = horas_trabalhadas*hora_ganha
print("+ Salário Bruto : R$"+str(salario_liquido))
print("- IR (11%) : R$"+str((salario_liquido/100)*11))
print("- INSS (8%) : R$"+str((salario_liquido/100)*8))
print("- Sindicato (5%) : R$"+str((salario_liquido/100)*5))
print("= Salário Líquido : R$"+str((salario_liquido/100)*76))