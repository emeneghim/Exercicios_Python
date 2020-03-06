"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um
 algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7"""

h = float(input("Insira a altura em metros: "))
sexo = input("Insira o seu sexo(M/F): ")
if sexo.upper() == "M":
    print("O seu peso ideal equivale a",str((72.7*h)-58)+"kg")
elif sexo.upper() == "F":
    print("O seu peso ideal equivale a",str((62.1*h)-44.7)+"kg")
else:
    print("Sexo nao valido!")