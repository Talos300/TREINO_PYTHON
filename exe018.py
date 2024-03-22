'''
Faça um programa que leia um ângulo qualquer e
mostre na tela o valo do seno, cosseno e tangente desse ângulo.
'''
import math

AQ = float (input("informe o angulo qualquer: "))

Cosseno = math.cos(math.radians(AQ))
Seno = math.sin(math.radians(AQ))
Tangente = math.tan(math.radians(AQ))

print("Cosseno: {:.2f} ".format(Cosseno))
print("Seno: {:.2f} ".format(Seno))
print("Tangente: {:.2f} ".format(Tangente))