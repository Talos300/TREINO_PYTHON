'''
Crie um programa que leia um número real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.
'''
import math #importa toda a biblioteca math, necessario infomrar a biblioteca e sua função para a aplicação
N = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua portção inteira é {}".format(N,math.trunc(N))) #(como não arredonda para maior ou menor, conserva o inteiro)
print("O valor digitado foi {} e a sua portção inteira é {}".format(N,math.floor(N))) #Arredpnda para menor na conversão
print("O valor digitado foi {} e a sua portção inteira é {}".format(N,math.ceil(N))) #Arredonda para maior na conversão

#OU COM BIBLIOTECA

#from math import trunc #Importe apenas a função  trunc
#N = float(input("Digite um valor: "))
#print("O valor digitado foi {} e a sua portção inteira é {}".format(N,trunc(N))) #necessario infomrar apenas a função puxada da biblioteca


#OU SEM BIBLIOTECA

#N = float (input("Informe um numero quebrado: \n"))
#print("O numero é {0} e sua versão inteira é {1}".format(N, int(N)))