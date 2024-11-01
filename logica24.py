import pandas as pd

# Criando um DataFrame com vendas de produtos em diferentes meses
dados_vendas = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
    'Janeiro': [200, 150, 300, 250],
    'Fevereiro': [220, 180, 280, 240],
    'Março': [250, 200, 320, 260],
    'Abril': [230, 170, 310, 270]
}

# Convertendo o dicionário para um DataFrame
df_vendas = pd.DataFrame(dados_vendas)

print("DataFrame com Vendas dos Produtos:")
print(df_vendas)

# Calculando a média de vendas por produto
df_vendas['Media_Vendas'] = df_vendas[['Janeiro', 'Fevereiro', 'Março', 'Abril']].mean(axis=1)

print("\nDataFrame com Médias de Vendas por Produto:")
print(df_vendas)

# Calculando a média geral das vendas
media_geral_vendas = df_vendas['Media_Vendas'].mean()
print("\nMédia geral das vendas:", round(media_geral_vendas, 2))
