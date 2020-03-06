"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e
a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""

arquivo = float(input("Insira quantos MB tem seu arquivo: "))
internet = float(input("Insira quantos Mbps tem sua internet: "))
segundos = arquivo/(internet/8)

print("O seu arquivo demorara aproximadamente",str(segundos/60),"minutos")