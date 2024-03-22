'''Desenvolva um programa que leia as duas notas de um aluno, calceule e mostre a sua mé´dia'''

nota_1 = float (input("Diga a sua nota da prmeira prova: "))
nota_2 = float (input("Diga a sua nota da segunda prova: "))

média_final = (nota_1 + nota_2) /2

print("Sua média final é {:.1f}".format(média_final))

