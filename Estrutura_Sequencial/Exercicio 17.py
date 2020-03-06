"""Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga
e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""

tamanho = float(input("Insira a quantidade de metros quadrados a serem pintados: "))
latas = tamanho//108
if tamanho%108 != 0:
    latas+=1
galoes = tamanho//21.6
if tamanho%21.6 != 0:
    galoes+=1
latas_mistura = tamanho//108
galoes_mistura = 0
resto = tamanho%108
if resto>0 and resto <=64.8:
    galoes_mistura = resto//21.6
elif resto>0 and resto >64.8:
    latas_mistura+=1
print("Comprando somente latas, equivale a um total de",str(latas)+", custando R$"+str(latas*80.00))
print("Comprando somente galoes, equivale a um total de ",str(galoes)+", custando R$"+str(galoes*25.00))
print("Misturando latas e galoes da forma mais barata, equivale a um total de",str(latas_mistura),"latas e",str(galoes_mistura),"galoes, totalizando R$"+str(latas_mistura*80.00+galoes_mistura*25))