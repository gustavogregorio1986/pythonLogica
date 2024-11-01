import pandas as pd

# Criando um DataFrame com vendas de produtos em diferentes meses
dados_vendas = {
    'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D', 'Produto E'],
    'Mes_1': [150, 200, 120, 180, 210],
    'Mes_2': [200, 250, 300, 220, 160],
    'Mes_3': [180, 220, 250, 230, 190]
}

# Convertendo o dicionário para um DataFrame
df_vendas = pd.DataFrame(dados_vendas)

print("DataFrame com Vendas de Produtos:")
print(df_vendas)

# Calculando a média de vendas por produto
df_vendas['Media_Vendas'] = df_vendas[['Mes_1', 'Mes_2', 'Mes_3']].mean(axis=1)

print("\nDataFrame com Médias de Vendas por Produto:")
print(df_vendas)

# Calculando a média geral de vendas por mês
media_geral_vendas = df_vendas[['Mes_1', 'Mes_2', 'Mes_3']].mean()
print("\nMédia geral de vendas por mês:")
print(media_geral_vendas.round(2))
