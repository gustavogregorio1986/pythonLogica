import pandas as pd

# Criando um DataFrame com vendas de produtos em diferentes regiões
dados_vendas = {
    'Regiao': ['Norte', 'Sul', 'Leste', 'Oeste'],
    'Vendas_Q1': [15000, 20000, 18000, 22000],
    'Vendas_Q2': [17000, 21000, 19000, 23000],
    'Vendas_Q3': [16000, 25000, 20000, 24000],
    'Vendas_Q4': [18000, 22000, 21000, 26000]
}

# Convertendo o dicionário para um DataFrame
df_vendas = pd.DataFrame(dados_vendas)

print("DataFrame com Vendas por Região:")
print(df_vendas)

# Calculando a média de vendas por região
df_vendas['Media_Vendas'] = df_vendas[['Vendas_Q1', 'Vendas_Q2', 'Vendas_Q3', 'Vendas_Q4']].mean(axis=1)

print("\nDataFrame com Médias de Vendas:")
print(df_vendas)

# Calculando a média geral das vendas
media_geral_vendas = df_vendas['Media_Vendas'].mean()
print("\nMédia geral das vendas:", round(media_geral_vendas, 2))
