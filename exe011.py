'''
Faça um programa que leia a largura e a altura de uma parede em metros, 
calcule a sua área e a quantidade de tinta necesária para pintá-la, 
sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float  (input("Informe a largura da parede: "))
altura =  float  (input("Informe a altura da parede: "))

area  = altura * largura
litro = area / 2
print("Sua parede tem a demissão de {}x{} e uma área de {}m²".format(largura,altura,area))
print("Você precisará de {}l para pintar essa parede".format(litro))
