numero_1 = int(input("Primeiro numero: "))
numero_2 = int(input("Segundo numero: "))

soma = numero_1 + numero_2 #mais
subtração = numero_1 - numero_2 #menos
multiplicação = numero_1 * numero_2 #vezes
divisão = numero_1 / numero_2 #dividir 
divisão_inteira = numero_1 // numero_2 #resto da divisão
potência = numero_1 ** numero_2 #pontencialização
print ("Soma é: {} subtração {} multiplicação é: {} divisão é {:.2f}".format(soma,subtração, multiplicação, divisão), end=" ")
print ("Divisão inteira (resto) {} e potência {}".format(divisão_inteira, potência))
