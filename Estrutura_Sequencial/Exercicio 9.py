#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * (F-32) / 9).

temp_F = float(input("Insira a temperatura em Farenheit: "))
temp_C = 5*(temp_F-32)/9
print("A temperatura",str(temp_F),"em Farenheit, equivale a",str(temp_C),"em graus Celsius.")