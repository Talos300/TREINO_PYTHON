"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

preço = float (input("Informe o valor do produto: "))
promo = float (input("Infomre a porcentagem da promoção: "))

desconto = preço * (promo / 100)
final = preço - desconto


print("Valor do produto é de {} e seu desconto é de {} é de \nEntão o valor final é de {}".format(preço,desconto,final))

