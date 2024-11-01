import pandas as pd

# Criando um DataFrame com vendas de representantes em diferentes dias
dados_vendas = {
    'Representante': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eduardo'],
    'Segunda': [500, 700, 300, 600, 400],
    'Terça': [600, 800, 400, 500, 300],
    'Quarta': [700, 600, 500, 400, 450],
    'Quinta': [800, 700, 600, 650, 300],
    'Sexta': [900, 950, 700, 800, 500]
}

# Convertendo o dicionário para um DataFrame
df_vendas = pd.DataFrame(dados_vendas)

print("DataFrame com Vendas dos Representantes:")
print(df_vendas)

# Calculando a média de vendas por representante
df_vendas['Media_Vendas'] = df_vendas[['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']].mean(axis=1)

print("\nDataFrame com Médias de Vendas por Representante:")
print(df_vendas)

# Calculando a média geral de vendas
media_geral_vendas = df_vendas['Media_Vendas'].mean()
print("\nMédia geral de vendas:", round(media_geral_vendas, 2))
