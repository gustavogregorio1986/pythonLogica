import pandas as pd

# Criando um DataFrame com frequência de alunos em aulas
dados_frequencia = {
    'Aluno': ['Lucas', 'Mariana', 'João', 'Ana', 'Rafael'],
    'Semana_1': [4, 3, 5, 2, 4],
    'Semana_2': [5, 3, 4, 5, 4],
    'Semana_3': [3, 4, 2, 4, 5],
    'Semana_4': [5, 5, 5, 4, 3]
}

# Convertendo o dicionário para um DataFrame
df_frequencia = pd.DataFrame(dados_frequencia)

print("DataFrame com Frequência dos Alunos em Aulas:")
print(df_frequencia)

# Calculando a média de presença por aluno
df_frequencia['Media_Frequencia'] = df_frequencia[['Semana_1', 'Semana_2', 'Semana_3', 'Semana_4']].mean(axis=1)

print("\nDataFrame com Médias de Frequência por Aluno:")
print(df_frequencia)

# Calculando a média geral de frequência
media_geral_frequencia = df_frequencia['Media_Frequencia'].mean()
print("\nMédia geral de frequência:", round(media_geral_frequencia, 2))
