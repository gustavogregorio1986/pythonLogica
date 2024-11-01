import pandas as pd

# Criando um DataFrame com horas trabalhadas por funcionários em diferentes dias
dados_horas = {
    'Funcionário': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eduardo'],
    'Segunda': [8, 7.5, 9, 8.5, 6],
    'Terça': [7, 8, 8.5, 7, 7.5],
    'Quarta': [8.5, 9, 7, 8, 6.5],
    'Quinta': [9, 8.5, 8, 9, 7],
    'Sexta': [8, 7, 8, 7.5, 8]
}

# Convertendo o dicionário para um DataFrame
df_horas = pd.DataFrame(dados_horas)

print("DataFrame com Horas Trabalhadas pelos Funcionários:")
print(df_horas)

# Calculando a média de horas trabalhadas por funcionário
df_horas['Media_Horas'] = df_horas[['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']].mean(axis=1)

print("\nDataFrame com Médias de Horas Trabalhadas por Funcionário:")
print(df_horas)

# Calculando a média geral de horas trabalhadas
media_geral_horas = df_horas['Media_Horas'].mean()
print("\nMédia geral de horas trabalhadas:", round(media_geral_horas, 2))
