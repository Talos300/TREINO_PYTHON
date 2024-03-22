'''
Faça um programa que leia um número 
Inteiro e mostre na tela o seu sucessor
e seu antecessor.
'''

numero = int (input("Diga um numero: "))

antecessor = (numero - 1)
sucessor = (numero + 1)

print("Seu numero é {} e seu sucessor é {} e seu antecessor é {} \n" .format (numero, sucessor, antecessor))

'''ou''' 
'''
numero = int (input("Diga um numero: "))

print("O seu numero é {} e seu antecessor é {} e seu sucessor é {} \n" .format (numero, (numero - 1), (numero + 1)))
'''