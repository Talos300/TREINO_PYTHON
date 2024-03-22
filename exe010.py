'''Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar'''
''' vamos considerar a cortão de 3,27'''

real = float (input("Informe quantos reais você possui na conta: "))


conversor = real / 3.27

print("Você pode converter {:.2f} reais em {:.2f} dolares ".format(real, conversor))