import pandas as pd

# Criando um DataFrame com despesas em diferentes categorias
dados_despesas = {
    'Categoria': ['Alimentação', 'Transporte', 'Lazer', 'Outros'],
    'Janeiro': [450, 120, 200, 300],
    'Fevereiro': [400, 150, 250, 280],
    'Março': [500, 130, 180, 320],
    'Abril': [480, 140, 210, 290],
    'Maio': [520, 160, 240, 310]
}

# Convertendo o dicionário para um DataFrame
df_despesas = pd.DataFrame(dados_despesas)

print("DataFrame com Despesas Mensais por Categoria:")
print(df_despesas)

# Calculando a média de despesas por categoria
df_despesas['Media_Despesas'] = df_despesas[['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio']].mean(axis=1)

print("\nDataFrame com Médias de Despesas por Categoria:")
print(df_despesas)

# Calculando a média geral das despesas
media_geral_despesas = df_despesas['Media_Despesas'].mean()
print("\nMédia geral das despesas:", round(media_geral_despesas, 2))
