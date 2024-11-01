import pandas as pd

# Criando um DataFrame com vendas de produtos em diferentes dias da semana
dados_vendas_produtos = {
    'Produto': ['Produto A', 'Produto B', 'Produto C'],
    'Segunda': [100, 150, 200],
    'Terça': [120, 160, 180],
    'Quarta': [130, 140, 190],
    'Quinta': [140, 130, 210],
    'Sexta': [150, 170, 220],
    'Sábado': [160, 180, 230],
    'Domingo': [180, 200, 240]
}

# Convertendo o dicionário para um DataFrame
df_vendas_produtos = pd.DataFrame(dados_vendas_produtos)

print("DataFrame com Vendas Diárias de Produtos:")
print(df_vendas_produtos)

# Calculando a média de vendas por produto
df_vendas_produtos['Media_Vendas'] = df_vendas_produtos[['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']].mean(axis=1)

print("\nDataFrame com Médias de Vendas:")
print(df_vendas_produtos)

# Calculando a média geral de vendas
media_geral_vendas = df_vendas_produtos['Media_Vendas'].mean()
print("\nMédia geral de vendas:", round(media_geral_vendas, 2))
