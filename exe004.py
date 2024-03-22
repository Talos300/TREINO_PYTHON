"""Faça um programa que leia algo pelo reclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele"""

dado = input("Digite uma senha: ")

print("O tipo primitivo desse dado é: ", type(dado))
print("Espacho vazio:", dado.isspace())
print("Apenas número", dado.isnumeric())
print("alfabético", dado.isalpha())
print("Alfanumérico", dado.isalnum())
print("Maiusculas", dado.isupper())
print("Minúsculas", dado.islower())
print("Capitalizada", dado.istitle())
