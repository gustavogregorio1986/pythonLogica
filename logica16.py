import pandas as pd

# Criando um DataFrame com vendas de produtos em diferentes meses
dados_vendas_produtos = {
    'Produto': ['Produto A', 'Produto B', 'Produto C'],
    'Mes1': [120, 200, 150],
    'Mes2': [130, 210, 160],
    'Mes3': [125, 205, 155],
    'Mes4': [140, 220, 165],
    'Mes5': [135, 215, 162],
    'Mes6': [150, 230, 170]
}

# Convertendo o dicionário para um DataFrame
df_vendas_produtos = pd.DataFrame(dados_vendas_produtos)

print("DataFrame com Vendas Mensais de Produtos:")
print(df_vendas_produtos)

# Calculando a média de vendas de cada produto
df_vendas_produtos['Media_Vendas'] = df_vendas_produtos[['Mes1', 'Mes2', 'Mes3', 'Mes4', 'Mes5', 'Mes6']].mean(axis=1)

print("\nDataFrame com Médias de Vendas:")
print(df_vendas_produtos)

# Calculando a média geral de vendas
media_geral_vendas = df_vendas_produtos['Media_Vendas'].mean()
print("\nMédia geral de vendas:", round(media_geral_vendas, 2))
