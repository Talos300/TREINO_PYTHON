'''faça um algoritmo que leia o sálario de um funcionário e mostre seu novo salário com 15% de aumento. '''

preço = float (input("Informe o  valor do produto: "))
promo = float (input("Infomre a porcentagem da promoção: "))

desconto = preço * (promo / 100)
final = preço - desconto


print("Valor do produto é de {} e seu desconto é de {} é de \nEntão o valor final é de {}".format(preço,desconto,final))