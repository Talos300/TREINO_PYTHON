'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por KM rodado. '''

KM = float (input("Quantos km seu carro andou ? "))
DIA = float (input("Quantos dias você ficou com ele ? "))

V_KM = (KM/1000) * 0.15
V_DIA = DIA * 60
V_F = V_DIA + V_KM

print("O valor a ser pago é: R${:.2f} ".format(V_F))