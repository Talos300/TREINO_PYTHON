'''
Um professor quer sortear um dos seus quatro
alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e
screvendo o nome do escolhido.
'''

import random

nome_1 = str (input("Primeiro nome: "))
nome_2 = str (input("Segundo nome: "))
nome_3 = str (input("Terceiro nome: "))
nome_4 = str (input("Quarto nome: "))

lista = [nome_1, nome_2, nome_3, nome_4]  #criado um vetor do mesmo tipo (str)

escolhido = random.choice(lista)

print("O escolhido é: {} ".format(escolhido))
