import pandas as pd

# Criando uma Série (vetor) com valores numéricos
vetor = pd.Series([10, 20, 30, 40, 50])

# Calculando a soma dos valores do vetor
soma_total = vetor.sum()
print("Vetor:")
print(vetor)
print("\nSoma total dos valores do vetor:", soma_total)
