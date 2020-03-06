#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

temp_C = float(input("Insira a temperatura em Celsius: "))
temp_F = temp_C*9/5+32
print("A temperatura",str(temp_C),"em Celsius, equivale a",str(temp_F),"em graus Farenheit.")