import pandas as pd

# Criando uma matriz 3x3 usando um DataFrame
matriz = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], columns=['Coluna1', 'Coluna2', 'Coluna3'])

print("Matriz 3x3:")
print(matriz)

# Soma de todos os elementos da matriz
soma_total = matriz.values.sum()
print("\nSoma total de todos os elementos da matriz:", soma_total)

# Soma dos elementos por coluna
soma_colunas = matriz.sum()
print("\nSoma dos elementos por coluna:")
print(soma_colunas)

# Soma dos elementos por linha
soma_linhas = matriz.sum(axis=1)
print("\nSoma dos elementos por linha:")
print(soma_linhas)
