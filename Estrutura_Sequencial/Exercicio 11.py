"""Faca um Programa que peça 2 numeros inteiros e um numero real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

num_a = int(input("Insira o valor A (inteiro): "))
num_b = int(input("Insira o valor B (inteiro): "))
num_c = float(input("Insira o valor C (real): "))

print("O produto do dobro do primeiro com metade do segundo equivale a", str((2*num_a) * (num_b/2)))
print("a soma do triplo do primeiro com o terceiro equivale a",str(num_a*3+num_c))
print("o terceiro elevado ao cubo equivale a",str(num_c**3))