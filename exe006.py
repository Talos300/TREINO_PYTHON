'''  Crie um algoritmo que leia um númer e mostre o seu dobro, tripo e raiz quadrada.'''

numero = float (input("Diga um numero: "))

dobro = numero * 2;
tripo = numero * 3;
raiz_quadrada = numero ** (1/2);

print(f"Seu dopro é: {dobro}");
print("Seu tripo é: {:.0f} \nSua riaz é: {:.2f}".format(tripo,raiz_quadrada));
