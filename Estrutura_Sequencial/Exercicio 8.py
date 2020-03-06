#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho_hora = float(input("Insira quanto voce ganha por hora: "))
horas_trabalhadas = int(input("Insira quantas horas voce trabalha no mes: "))
print ("Sua renda mensal sera de R$"+str(ganho_hora*horas_trabalhadas))