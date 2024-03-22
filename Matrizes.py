'''
Matrizes em Python são representadas como
listas de listas, onde cada lista interna 
representa uma linha da matriz.
'''

# Declarando uma matriz (lista de listas)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Acessando elementos da matriz
print("Elemento na linha 2, coluna 3:", matriz[1][2])  # Índices são baseados em zero

# Iterando sobre a matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Para imprimir uma nova linha após cada linha da matriz
