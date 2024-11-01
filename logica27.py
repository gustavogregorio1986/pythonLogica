import pandas as pd

# Criando um DataFrame com despesas mensais de diferentes pessoas
dados_despesas = {
    'Pessoa': ['Lucas', 'Mariana', 'João', 'Ana', 'Rafael'],
    'Alimentacao': [500, 600, 550, 700, 450],
    'Transporte': [200, 150, 300, 250, 400],
    'Lazer': [150, 200, 100, 250, 300]
}

# Convertendo o dicionário para um DataFrame
df_despesas = pd.DataFrame(dados_despesas)

print("DataFrame com Despesas Mensais:")
print(df_despesas)

# Calculando a média de despesas por pessoa
df_despesas['Media_Despesas'] = df_despesas[['Alimentacao', 'Transporte', 'Lazer']].mean(axis=1)

print("\nDataFrame com Médias de Despesas por Pessoa:")
print(df_despesas)

# Calculando a média geral de despesas por categoria
media_geral_despesas = df_despesas[['Alimentacao', 'Transporte', 'Lazer']].mean()
print("\nMédia geral de despesas por categoria:")
print(media_geral_despesas.round(2))
