import pandas as pd

# Criando um DataFrame com nomes de pessoas e suas despesas em três categorias
dados_despesas = {
    'Nome': ['Lucas', 'Mariana', 'João', 'Fernanda', 'Pedro'],
    'Alimentacao': [500, 600, 450, 700, 300],
    'Transporte': [150, 200, 100, 250, 80],
    'Lazer': [200, 250, 150, 300, 100]
}

# Convertendo o dicionário para um DataFrame
df_despesas = pd.DataFrame(dados_despesas)

print("DataFrame com Despesas Mensais:")
print(df_despesas)

# Calculando a média de despesas de cada pessoa
df_despesas['Media_Despesas'] = df_despesas[['Alimentacao', 'Transporte', 'Lazer']].mean(axis=1)

print("\nDataFrame com Despesas e Médias:")
print(df_despesas)

# Calculando a média geral das despesas
media_geral_despesas = df_despesas['Media_Despesas'].mean()
print("\nMédia geral das despesas:", round(media_geral_despesas, 2))
