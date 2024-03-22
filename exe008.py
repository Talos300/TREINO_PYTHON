"""Escrava um programa que leia um valor em metros e o exiba convertido em centimetos e milimetros"""

metro = float (input("Informe a medida do metro: "))


milimetro = metro / 1000
centrimeto = metro / 100
decimetro = metro / 10

decametro = metro * 10
hectometro = metro * 100
quilometro = metro * 1000

print("A medida de metros {} em: \nMilimetros é: {} \nCentrimetos é: {}\nDecimetros é: {} \n".format(metro, milimetro, centrimeto, decimetro))
print("Decamentro é: {} \nHectometro é: {} \nQuilometro é: {}".format (decametro, hectometro, quilometro))
