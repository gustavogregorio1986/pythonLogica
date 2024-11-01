import pandas as pd

# Criando um DataFrame com notas de estudantes em diferentes disciplinas
dados_notas = {
    'Estudante': ['João', 'Maria', 'Pedro', 'Ana', 'Carlos'],
    'Matematica': [8.5, 9.0, 7.5, 6.0, 8.0],
    'Portugues': [7.0, 8.5, 9.0, 8.0, 7.5],
    'Ciencias': [9.0, 7.5, 8.0, 9.5, 8.0]
}

# Convertendo o dicionário para um DataFrame
df_notas = pd.DataFrame(dados_notas)

print("DataFrame com Notas dos Estudantes:")
print(df_notas)

# Calculando a média de notas por estudante
df_notas['Media_Notas'] = df_notas[['Matematica', 'Portugues', 'Ciencias']].mean(axis=1)

print("\nDataFrame com Médias de Notas por Estudante:")
print(df_notas)

# Calculando a média geral das notas
media_geral_notas = df_notas[['Matematica', 'Portugues', 'Ciencias']].mean()
print("\nMédia geral das notas:")
print(media_geral_notas.round(2))
