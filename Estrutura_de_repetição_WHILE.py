#WHILE 
'''é uma estrutura de controle de fluxo que 
permite executar repetidamente um bloco de código
até a condição for verdadeira'''

'''
while condição:
    # bloco de código a ser repetido enquanto a condição for verdadeira
'''

#Contagem regressiva até zero:
contador = 5

while contador > 0:
    print(contador)
    contador -= 1

print("Fogo!")

'''
#Soma dos primeiros N números naturais:
soma = 0
n = 1
limite = 10

while n <= limite:
    soma += n
    n += 1

print("A soma dos primeiros", limite, "números naturais é:", soma)

#Perguntando ao usuário até receber uma resposta válida: 
resposta = ""
while resposta.lower() not in ("sim", "não"):
    resposta = input("Você deseja continuar? (sim/não): ")

print("Resposta válida recebida:", resposta)
'''
