'''
Faça um programa que leia o comprimento do
cateto oposto e da cateto adjacente de um triangulo retangulo, 
calcule e mostre o comprimento da hipotenusa.
'''
#calcular a raiz quadrada de algo: ** (1/2), use a pontencialização sobre a fração (1/2)

# feito com import com uma função

from math import sqrt

CO = float (input("informe o Cateto Oposto: "))
CA = float (input("Informe o Cateto Adjacente: "))

HI = CO ** 2 + CA ** 2

print("Sua ipotenusa é:  {:.3f}".format(sqrt(HI)))


#         feito sem import
'''
CO = float (input("informe o Cateto Oposto: "))
CA = float (input("Informe o Cateto Adjacente: "))
CO_2 = CO ** 2
CA_2 = CA ** 2
HI = CO_2 + CA_2
HI_2 = HI ** (1/2)

#print(f"Sua hipotenusa é: {HI_2}") 
#               OU
print("Sua hipotenusa é: {:.2f}".format(HI_2))

''' 

# feito com import completo
'''
import math

CO = float (input("informe o Cateto Oposto: "))
CA = float (input("Informe o Cateto Adjacente: "))

HI = CO ** 2 + CA ** 2

print("Sua ipotenusa é:  {:.3f}".format(math.sqrt(HI)))
'''